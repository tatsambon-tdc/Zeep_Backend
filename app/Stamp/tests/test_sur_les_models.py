"""
Tests sur les models de l'application Stamp
"""

from django.db import IntegrityError
from django.test import TestCase
from unittest.mock import patch

from Stamp.models import PatternStamp, PatternStamp_image_file_path

from .utilities import create_forme, create_user


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

        }
        PatternStamp_de_test_created = PatternStamp.objects.create(
            **PatternStamp_de_test)

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

        }
        PatternStamp_de_test2 = {

            "creator": user,
            "titre": "Titre Du paternStamp de test",
            "forme": forme,

        }

        PatternStamp_de_test1 = PatternStamp.objects.create(
            **PatternStamp_de_test1)
        with self.assertRaises(IntegrityError):
            PatternStamp.objects.create(**PatternStamp_de_test2)

    @patch('Stamp.models.uuid.uuid4')
    def test_patternStamp_image_example_file_name(self, mock_uuid):
        """Test  de la generation des chemin des image"""

        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = PatternStamp_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/PatternStamp/{uuid}.jpg')
