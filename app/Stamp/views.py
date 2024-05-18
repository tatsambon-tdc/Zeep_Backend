"""Ici toute les vues de l'apa Stamp """

from rest_framework import viewsets

from .models import PatternStamp, Monture
from . import serializers
from .permissions import IsStaff
from rest_framework.authentication import TokenAuthentication


class MyViewSetsMinIn():
    """Pour les element commun aux viesets"""
    serializer_class = None
    serializer_detail_class = None

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_class

        return self.serializer_detail_class


class PatternStampViewSet(MyViewSetsMinIn, viewsets.ReadOnlyModelViewSet):
    """
    Lecture des Patternstamp Pour
    les users
    """
    queryset = PatternStamp.objects.all()
    serializer_class = serializers.PatternStampSerializer
    serializer_detail_class = serializers.PatternStampDetailSerializer


class AdminPatternStampViewSet(MyViewSetsMinIn, viewsets.ModelViewSet):
    """
    L'administration des PatterStamp
    """
    queryset = PatternStamp.objects.all()
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]

    serializer_class = serializers.PatternStampSerializer
    serializer_detail_class = serializers.PatternStampDetailSerializer

# -------------------------------------------------------------------


class MontureViewSet(MyViewSetsMinIn, viewsets.ReadOnlyModelViewSet):
    """
    Lecture des Patternstamp
    """
    queryset = Monture.objects.all()
    serializer_class = serializers.MontureSerializer
    serializer_detail_class = serializers.MontureDetailSerializer


class AdminMontureViewSet(MyViewSetsMinIn, viewsets.ModelViewSet):
    """
    L'administration des PatterStamp
    """
    queryset = Monture.objects.all()
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]

    serializer_class = serializers.MontureSerializer
    serializer_detail_class = serializers.MontureDetailSerializer
