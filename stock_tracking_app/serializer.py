from dataclasses import fields
from rest_framework import serializers
from .models import stock_tracking_model
from .models import product_model

class stockserializer(serializers.ModelSerializer):
    class Meta:
        model = stock_tracking_model
        fields = '__all__'

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = product_model
        fields = '__all__'

