from django.db.models import fields
from rest_framework import serializers
from istore.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','get_thumbnail', 'description', 'price', 'name','get_absolute_url')
        


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'