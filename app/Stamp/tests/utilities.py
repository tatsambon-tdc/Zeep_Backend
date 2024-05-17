"""Lest fonctions constamant appelée dans nos
test"""


from django.contrib.auth import get_user_model
from Stamp.models import PatternStamp, Forme


def create_user(email, password):
    """Creation et renvoie d'un User
    utilisable pour la creation d'un
    PatternStamp"""

    return get_user_model().objects.create_user(email=email, password=password)


def create_superuser(email, password):
    """Creation et renvoie d'un User
    utilisable pour la creation d'un
    PatternStamp"""

    return get_user_model().objects.create_superuser(
        email=email,
        password=password
        )


def create_PatternStamp(donnees):
    """Creation et renvoie d'un PatternStamp"""
    return PatternStamp.objects.create(**donnees)


def create_forme(forme):

    """Creation et renvoie d'une Forme
    utilisable pour la creation d'un
    PatternStamp"""

    return Forme.objects.create(forme=forme)
