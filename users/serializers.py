from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Unicorn


class UnicornSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unicorn
        fields = ('name', 'age')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

# https://medium.com/halfspring/guide-to-an-oauth2-api-with-django-6ba66a31d6d@