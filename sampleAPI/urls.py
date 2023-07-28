from django.urls import path
from .views import productAPIView, tokenView as tokenview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("products/", productAPIView.as_view(), name="productview"),
    path("token/", obtain_auth_token),
]
