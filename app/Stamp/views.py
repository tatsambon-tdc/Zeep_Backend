"""Ici toute les vues de l'apa Stamp """

from rest_framework import viewsets

from .models import PatternStamp
from . import serializers
from .permissions import IsStaff
from rest_framework.authentication import TokenAuthentication


class PatternStampViewSet(viewsets.ModelViewSet):
    """Viewser pour la gession de
    l'api du model PatterStamp
    """
    queryset = PatternStamp.objects.all()
    authentication_classes = []
    permission_classes = []

    def get_permissions(self):
        """
        Instantiates and returns the list
        of permissions that this view requires.
        """
        if self.request.method in ['POST', 'DELETE', 'PATCH']:

            self.authentication_classes.append(TokenAuthentication)
            self.permission_classes.append(IsStaff)
            return [permission() for permission in self.permission_classes]
        return []

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PatternStampSerializer

        return serializers.PatternStampDetailSerializer
