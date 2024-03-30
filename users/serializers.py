from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CreateEvent
from django.contrib.auth.forms import UserCreationForm,authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")




class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateEvent
        fields = ['id', 'title', 'content', 'location', 'organizer', 'created_at']