from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterationForm, productForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import customUser
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from .models import productImage, products
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import imageUploadForm
from .models import loggers2


def show_product_images(request):
    # Fetch all product images from the database
    images = productImage.objects.all()

    # Pass the images to the template
    return render(request, "register/product_images.html", {"images": images})


@login_required
def edit(request, product_id):
    if products.objects.get(id=product_id).user_id == request.user.id:
        if request.method == "POST":
            form = productForm(
                request.POST, instance=products.objects.get(id=product_id)
            )
            if form.is_valid():
                form.save()
                return redirect("dashboard")
        else:
            form = productForm(instance=products.objects.get(id=product_id))
        return render(
            request,
            "register/edit.html",
            {"form": form, "product": products.objects.get(id=product_id)},
        )
    else:
        return HttpResponse("NOT AUTHENTICATED")


@login_required
def show_images(request, product_id):
    if products.objects.get(id=product_id).user_id == request.user.id:
        product_details = products.objects.get(id=product_id)
        image_list = productImage.objects.filter(product_id=product_details.id)
        return render(request, "register/show_images.html", {"image_list": image_list})
    else:
        return HttpResponse("NOT AUTHENTICATED")


@login_required
def image_add(request, product_id):
    if products.objects.get(id=product_id).user_id == request.user.id:
        prodt = products.objects.get(id=product_id)
        product_images = productImage.objects.filter(product=prodt)
        if len(product_images) < 6:
            if request.method == "POST":
                form = imageUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    image = form.save(commit=False)
                    image.product_id = product_id
                    image.save()
                    return redirect("dashboard")
            else:
                form = imageUploadForm()
        else:
            return HttpResponse("YOU CANNOT UPLOAD ANY MORE IMAGES")
        return render(
            request, "register/image_add.html", {"form": form, "product": prodt.name}
        )
    else:
        return HttpResponse("NOT AUTHENTICATED")


@login_required
def addProduct(request):
    form = productForm()

    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            user_id = request.user.id
            product.user_id = user_id
            product.save()
            return redirect("added_product")

    return render(request, "register/addproduct.html", {"form": form})


@login_required
def product_added(request):
    lastest_addded_product = products.objects.last()
    return render(
        request, "register/product_added.html", {"product": lastest_addded_product}
    )


def logging(request):
    log = loggers2.objects.all()
    return render(request, "register/logg.html", {"loggers": log})


@login_required
def resetPassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("dashboard")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "register/reset_pwd.html", {"form": form})


class userview(ListView):
    model = customUser
    template_name = "register/userview.html"
    context_object_name = "users"


def register(response):
    form = RegisterationForm(response.POST)
    if response.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            raise ValidationError("Form is not valid.")
    return render(response, "register/register.html", {"form": form})


def home(response):
    return render(
        response,
        "register/home.html",
        {"user": response.user},
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm(request)
    return render(request, "register/login.html", {"form": form})


def success(request):
    return HttpResponse("THE USER HAS BEEN REGISTERED")


def logout_view(request):
    logout(request)
    return redirect("home")


from django.db.models import Prefetch


class dashboardView(LoginRequiredMixin, TemplateView):
    template_name = "register/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_with_images = products.objects.filter(
            user_id=self.request.user.id
        ).prefetch_related(
            Prefetch(
                "productimage_set",
                queryset=productImage.objects.order_by("id"),
                to_attr="images",
            )
        )

        context["products"] = products_with_images
        context["user"] = self.request.user

        return context
