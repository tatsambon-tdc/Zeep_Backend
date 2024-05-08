"""
Serializer pour  la View de l'api User
"""

from django.contrib.auth import (
            get_user_model,
            authenticate,

            )
from rest_framework import serializers

# fonction de traduction
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    """Le serializer du model User"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, donnees_ok):
        """Creation et renvoi se l'user avec le mode pass chifé """

        return get_user_model().objects.create_user(**donnees_ok)

    def update(self, instance, validated_data):
        """Update and return user."""

        print('une mise a jour est en ours ')
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Le serializer pour les token user"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validation det authentification du user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
            )

        if not user:
            message = _("Impossible de vous authentifiez ! \
                veriffiez vos identifiants")
            raise serializers.ValidationError(message)

        attrs['user'] = user
        return attrs
