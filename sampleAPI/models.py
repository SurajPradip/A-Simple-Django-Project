from django.db import models
from register.models import products, productImage, customUser
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


@receiver(post_save, sender=customUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print(f"TOKEN CREATED {Token.objects.get(user=instance)}")
