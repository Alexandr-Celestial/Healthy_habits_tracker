from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = "__all__"

class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания User"""

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        user: User = User.objects.create(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user