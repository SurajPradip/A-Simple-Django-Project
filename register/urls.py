from django.urls import path
from .views import register, home, login_view, success
from .views import userview, logout_view, dashboardView
from .views import resetPassword, addProduct, product_added
from .views import image_add, show_images, edit
from django.conf import settings
from django.conf.urls.static import static
from .views import logging, show_product_images


urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("success/", home, name="success"),
    path("userview/", userview.as_view()),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboardView.as_view(), name="dashboard"),
    path("reset_password/", resetPassword, name="change_pwd"),
    path("add_product/", addProduct, name="add_product"),
    path("added_product/", product_added, name="added_product"),
    path("add_image/<int:product_id>/", image_add, name="image_add"),
    path("show_images/<int:product_id>/", show_images, name="show_images"),
    path("edit/<int:product_id>/", edit, name="edit"),
    path("logs/", logging, name="logs"),
    path("images/", show_product_images, name="product_images"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
