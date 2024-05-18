"""Ici les serializers de tout nos model """

from rest_framework import serializers

from .models import (
    PatternStamp,
    Monture
    )


class PatternStampSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre']


class PatternStampDetailSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre', 'forme', 'creator']


class MontureSerializer(serializers.ModelSerializer):
    """Serializer de liste de Monture """

    class Meta:
        model = Monture
        fields = ['id', 'prix', 'name', 'forme', 'type']


class MontureDetailSerializer(serializers.ModelSerializer):
    """Serializer de detail de Monture """

    class Meta:
        model = Monture
        fields = ['prix', 'name', 'forme', 'type', 'creator']
