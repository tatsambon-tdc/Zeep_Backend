"""Ici les serializers de tout nos model """

from rest_framework import serializers

from .models import (
    PatternStamp,
    Monture,
    Encrier,
    PaieAccount

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
# -------------------------------------------------------------
#
#   Serialiser du model  MONTURE
#
# -------------------------------------------------------------


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
# -------------------------------------------------------------
#
#   Serialiser du model  ENCRIER
#
# -------------------------------------------------------------


class EncrierSerializer(serializers.ModelSerializer):
    """Serializer de liste de Encrier """

    class Meta:
        model = Encrier
        fields = ['id',  'couleur', 'disponible', ]


class EncrierDetailSerializer(serializers.ModelSerializer):
    """Serializer de detail de Encrier """

    class Meta:
        model = Encrier
        fields = ['id', 'prix', 'couleur', 'disponible', 'creator']

# -------------------------------------------------------------
#
#   Serialiser du model  PaieAccount
#
# -------------------------------------------------------------


class PaieAccountSerializer(serializers.ModelSerializer):
    """Serializer de PaieAccount """

    class Meta:
        model = PaieAccount
        fields = '__all__'
