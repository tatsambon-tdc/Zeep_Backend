"""Ici les serializers de tout nos model """

from rest_framework import serializers

from .models import (
    Commande,
    PatternStamp,
    Monture,
    Encrier,
    PaieAccount,
    Paiement

    )


class PatternStampSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre', 'image']


class PatternStampDetailSerializer(serializers.ModelSerializer):
    """Serializer de liste pour le model
    PatternStamp"""

    class Meta:
        model = PatternStamp
        fields = ['id', 'titre', 'forme', 'creator', 'image']
# -------------------------------------------------------------
#
#   Serialiser du model  MONTURE
#
# -------------------------------------------------------------


class MontureSerializer(serializers.ModelSerializer):
    """Serializer de liste de Monture """

    class Meta:
        model = Monture
        fields = ['id', 'prix', 'name', 'forme', 'type', 'image']


class MontureDetailSerializer(serializers.ModelSerializer):
    """Serializer de detail de Monture """

    class Meta:
        model = Monture
        fields = ['prix', 'name', 'forme', 'type', 'creator', 'image']
# -------------------------------------------------------------
#
#   Serialiser du model  ENCRIER
#
# -------------------------------------------------------------


class EncrierSerializer(serializers.ModelSerializer):
    """Serializer de liste de Encrier """

    class Meta:
        model = Encrier
        fields = ['id',  'couleur', 'disponible', 'image']


class EncrierDetailSerializer(serializers.ModelSerializer):
    """Serializer de detail de Encrier """

    class Meta:
        model = Encrier
        fields = ['id', 'prix', 'couleur', 'disponible', 'creator', 'image']

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

# -------------------------------------------------------------
#
#   Serialiser du model  PAIEMENT
#
# -------------------------------------------------------------


class PaiementSerializer(serializers.ModelSerializer):
    """Serializer de PaieAccount """

    class Meta:
        model = Paiement
        fields = '__all__'


# -------------------------------------------------------------
#
#   Serialiser du model  Commande
#
# -------------------------------------------------------------

class CommandeSerializer(serializers.ModelSerializer):
    """Serializer de PaieAccount """

    class Meta:
        model = Commande
        fields = '__all__'
