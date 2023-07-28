from register.models import products
from rest_framework.serializers import ModelSerializer


class productSerializer(ModelSerializer):
    class Meta:
        model = products
        fields = ["name", "price", "SKU", "description"]
