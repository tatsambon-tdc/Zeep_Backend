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
ADMINPATTERNSTAMP_URL = reverse('Stamp:adminPatternStamp-list')


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
            'prix': Decimal('85.50'),
            'titre': 'Test PatternStam1'
        }
        self.patterStamp = utilities.create_PatternStamp(self.dic)
        self.PATTERNSTAMP_URL_DETAIL = reverse(
            'Stamp:patternstamp-detail',
            kwargs={'pk': self.patterStamp.pk}
            )

        self.client = APIClient()

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
        self.assertEqual(Decimal(res.data['prix']), self.patterStamp.prix)

    def test_si_la_creation_ne_fonctione_pas(self):
        """Pour un user visiteur ou non peut
        fair un POST"""

        res = self.client.post(PATTERNSTAMP_URL, kwargs=self.dic)
        self.assertNotEqual(res.status_code, status.HTTP_201_CREATED)

    def test_si_la_suppression_ne_fonctione_pas(self):
        """Pour un user visiteur ou non peut
        fair un DELETE"""

        res = self.client.delete(
            self.PATTERNSTAMP_URL_DETAIL,
            kwargs=self.patterStamp.pk
            )

        self.assertNotEqual(res.status_code, status.HTTP_204_NO_CONTENT)
