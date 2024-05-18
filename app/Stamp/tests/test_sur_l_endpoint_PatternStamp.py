"""
Test sur les enpoints de l'API des
PATTERNSTAMP
"""

from decimal import Decimal
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from . import utilities

PATTERNSTAMP_URL = reverse('Stamp:patternstamp-list')
MONTURE_URL = reverse('Stamp:monture-list')
ENCRIER_URL = reverse('Stamp:encrier-list')
PAIEACCOUNT_URL = reverse('Stamp:adminPaieAccount-list')


class PublicPatternStampTests(TestCase):

    """Les tes qui ne demande pas a cequie l'user
    soit connecté
    """
    def setUp(self):
        self.user = utilities.create_user(
            email="public@user.cm",
            password="plublicTestUserOass")
        self.forme = utilities.create_forme(forme="ROND")
        self.dic = {
            'creator': self.user,
            'forme': self.forme,
            'titre': 'Test PatternStam1',
        }
        self.patterStamp = utilities.create_PatternStamp(self.dic)
        self.PATTERNSTAMP_URL_DETAIL = reverse(
            'Stamp:patternstamp-detail',
            kwargs={'pk': self.patterStamp.pk}
            )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_accessible(self):
        """Test si l'endpoint de liste
        fonctionne normalement """

        res = self.client.get(PATTERNSTAMP_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['id'], self.patterStamp.id)

    def test_detail_accessible(self):
        """Test si l'endpoint de liste
        fonctionne normalement """

        res = self.client.get(self.PATTERNSTAMP_URL_DETAIL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], self.patterStamp.id)
        self.assertEqual(res.data['creator'], self.patterStamp.creator.pk)
        self.assertEqual(res.data['forme'], self.patterStamp.forme.pk)

    def test_si_la_creation_ne_fonctione_pas(self):
        """Pour un user visiteur ou non peut
        fair un POST"""

        res = self.client.post(PATTERNSTAMP_URL, kwargs=self.dic)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_si_la_suppression_ne_fonctione_pas(self):
        """Pour un user visiteur ou non peut
        fair un DELETE"""

        res = self.client.delete(
            self.PATTERNSTAMP_URL_DETAIL,
            kwargs=self.patterStamp.pk
            )

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class PublicMontureTests(TestCase):

    """Les tes qui ne demande pas a cequie l'user
    soit connecté
    """
    def setUp(self):
        self.user = utilities.create_user(
            email="public@user.cm",
            password="plublicTestUserOass")
        self.forme = utilities.create_forme(forme="ROND")
        self.type = utilities.create_type(type="METALIQUE")
        self.dic = {
            'creator': self.user,
            'forme': self.forme,
            'name': 'nom  de la monture',
            'prix': '52.20',
            'type': self.type
        }
        self.monture = utilities.create_Monture(self.dic)
        self.MONTURE_URL_DETAIL = reverse(
            'Stamp:monture-detail',
            kwargs={'pk': self.monture.pk}
            )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_accessible(self):
        """Test si l'endpoint de liste
        fonctionne normalement """

        res = self.client.get(MONTURE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['id'], self.monture.id)

    def test_detail_accessible(self):
        """Test si l'endpoint de liste
        fonctionne normalement """

        res = self.client.get(self.MONTURE_URL_DETAIL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['creator'], self.monture.creator.pk)
        self.assertEqual(res.data['forme'], self.monture.forme.pk)
        self.assertEqual(res.data['name'], self.monture.name)
        self.assertEqual(res.data['prix'], self.monture.prix)


class PublicEncrierTests(TestCase):
    """Test des appels publique
    sur l'API de monture
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = utilities.create_user(
            'test@mail.xi',
            "testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_si_la_liste_est_assecible(self):
        """Test sur l'endpoint de liste"""

        donnee = {
            'couleur': 'Noir',
            'disponible': True,
            'creator': self.user,
            'prix': Decimal('525.20')

        }
        encrier_de_test = utilities.create_encrier(donnee)

        res = self.client.get(ENCRIER_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]['disponible'], encrier_de_test.disponible)
        self.assertEqual(res.data[0]['couleur'], encrier_de_test.couleur)


class PublicPaieAccountTests(TestCase):
    """Tests des appels pubblic sur l'api PaieAccount"""

    def setUp(self) -> None:
        self.user = utilities.create_user(
            'test@tes.tes',
            'gfgfd')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_si_l_la_liste_est_refusee(self):

        res = self.client.get(PAIEACCOUNT_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
