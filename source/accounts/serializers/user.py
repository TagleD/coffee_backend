from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Level

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['phone']


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    next_level_beans = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'avatar', 'beans', 'beans_total', 'level', 'next_level_beans']

    def get_level(self, user):
        return Level.objects.filter(beans_required__lte=user.beans_total).count() - 1

    def get_next_level_beans(self, user):
        current_level = Level.objects.filter(beans_required__lte=user.beans_total).count() - 1
        next_level = Level.objects.filter(number=current_level + 1).first()
        return next_level.beans_required if next_level else None


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'avatar']
