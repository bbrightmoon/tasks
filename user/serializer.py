from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import User


class RegisUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError('email is already in use')

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('already exists')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)

        user.set_password(password)

        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=5,
                                   max_length=40,
                                   )
    username = serializers.CharField(min_length=3,
                                     max_length=255
                                     )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
                  ]


class SearchSerializer(serializers.Serializer):
    def validate_search(self, obj):
        if isinstance(obj, User):
            serializer = LoginSerializer(obj)
        else:
            raise Exception("Nothing found!")
        return serializer.data