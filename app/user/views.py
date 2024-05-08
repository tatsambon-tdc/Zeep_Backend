"""
les Views Pour notre api User
"""
# Create your views here.

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (
        UserSerializer,
        AuthTokenSerializer,
        )


class CreateUserView(generics.CreateAPIView):
    """Creation d'un user grace a l'api"""

    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Gestion des user authentifiés"""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Recuperationet retour de l'user authentifié"""

        return self.request.user


class CreateTokenView(ObtainAuthToken):
    """Creation d'un tokrn  user grace a l'api"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
