from django.shortcuts import render
from register.models import products
from rest_framework.generics import ListCreateAPIView
from .serializers import productSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from register.models import customUser
from django.http import HttpResponse


for user in customUser.objects.all():
    Token.objects.get_or_create(user=user)


def tokenView(request):
    return HttpResponse(request.auth)


class productAPIView(LoginRequiredMixin, ListCreateAPIView):
    model = products
    serializer_class = productSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return products.objects.all()
