"""Ici toute les vues de l'apa Stamp """

from rest_framework import viewsets

from .models import PatternStamp
from . import serializers
from .permissions import IsStaff
from rest_framework.authentication import TokenAuthentication


class MyViewSetsMinIn():
    """Pour les element commun aux viesets"""
    serializer_liste_class = []
    serializer_detail_class = []

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_liste_class

        return self.serializer_detail_class


class PatternStampViewSet(MyViewSetsMinIn, viewsets.ReadOnlyModelViewSet):
    """
    Lecture des Patternstamp
    """
    queryset = PatternStamp.objects.all()
    serializer_liste_class = serializers.PatternStampSerializer
    serializer_detail_class = serializers.PatternStampDetailSerializer


class AdminPatternStampViewSet(viewsets.ModelViewSet):
    """
    L'administration des PatterStamp
    """
    queryset = PatternStamp.objects.all()
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]

    serializer_liste_class = serializers.PatternStampSerializer
    serializer_detail_class = serializers.PatternStampDetailSerializer
