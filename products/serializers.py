from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product2, User, Log,Purchase,Cart

class Product2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product2
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        #user.set_password(validated_data['password'])
        user.save()
        return user

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

