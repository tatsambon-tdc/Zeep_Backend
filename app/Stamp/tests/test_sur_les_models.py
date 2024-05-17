"""
Tests sur les models de l'application Stamp
"""

from django.db import IntegrityError
from django.test import TestCase

from Stamp.models import PatternStamp, Forme
from decimal import Decimal

from django.contrib.auth import get_user_model


def create_user(email, password):
    """Creation et renvoie d'un User
    utilisable pour la creation d'un
    PatternStamp"""

    return get_user_model().objects.create_user(email=email, password=password)


def create_PatternStamp(donnees):
    """Creation et renvoie d'un PatternStamp"""
    return PatternStamp.objects.create(**donnees)


def create_forme(forme):

    """Creation et renvoie d'une Forme
    utilisable pour la creation d'un
    PatternStamp"""

    return Forme.objects.create(forme=forme)


class PuclicModelPatternStampTest(TestCase):
    """Test si l'instance de PatternStamp est
    crée
    """

    def test_de_la_creation_d_un_PatternStamp(self):
        """Test si cration fonctione bien"""
        user = create_user(
            "email@user.com",
            "thespass",
        )

        forme = create_forme(forme='Rond')

        PatternStamp_de_test = {

            "creator": user,
            "titre": "Titre Du paternStamp de test",
            "forme": forme,
            "prix": Decimal('5.5'),

        }
        PatternStamp_de_test_created = PatternStamp.objects.create(
            **PatternStamp_de_test)

        self.assertEqual(PatternStamp_de_test["prix"],
                         PatternStamp_de_test_created.prix)
        self.assertEqual(PatternStamp_de_test["forme"],
                         PatternStamp_de_test_created.forme)

        self.assertEqual(PatternStamp_de_test["titre"],
                         PatternStamp_de_test_created.titre)

    def test_sur_l_unicite_du_titre(self):
        """Test si plusieurs instances de
        PatternStamp Peuvent avoir le
        meme titre"""

        user = create_user(
            "email@user.com",
            "thespass"
        )
        forme = create_forme(forme='Rond')

        PatternStamp_de_test1 = {
            "creator": user,
            "titre": "Titre Du paternStamp de test",
            "forme": forme,
            "prix": Decimal('5.5'),

        }
        PatternStamp_de_test2 = {

            "creator": user,
            "titre": "Titre Du paternStamp de test",
            "forme": forme,
            "prix": Decimal('5.5'),

        }

        PatternStamp_de_test1 = PatternStamp.objects.create(
            **PatternStamp_de_test1)
        with self.assertRaises(IntegrityError):
            PatternStamp.objects.create(**PatternStamp_de_test2)
