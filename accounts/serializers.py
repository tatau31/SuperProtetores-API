from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf', 'email')

class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cpf', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError ({"password": "Senhas não conferem"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password já que não é necessário para criar o usuário
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            cpf=validated_data['cpf'],
            username = validated_data['first_name'] + ' ' + validated_data['last_name']
        )
        return user
    
    
class LoginSerializer(serializers.Serializer):
    pass