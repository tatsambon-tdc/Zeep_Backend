"""Ici les serializers de tout nos model """

from rest_framework import serializers

from .models import PatternStamp


class PatternStampSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre']
        read_only_fields = ['id']


class PatternStampDetailSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre', 'forme', 'prix']
