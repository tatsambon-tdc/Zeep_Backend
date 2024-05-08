"""
les test sur l'api user
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    """Creation et renvoi d'un user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """Test des fonctionnalite publique de l'api user
    qui ne demander pas d'aythentification"""

    def setUp(self):
        self.client = APIClient()

    def test_creation_de_l_user_a_reuissi(self):
        """Test si la creation d'un user via l'api fonctionne"""

        donnees = {
            'email': 'test@email.com',
            'password': 'pv9Si8CyB2y355FW',
            'name': 'kiortest',
        }

        res = self.client.post(CREATE_USER_URL, donnees)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=donnees['email'])
        self.assertTrue(user.check_password(donnees['password']))

    def test_si_l_email_existe_deja(self):
        """Test si il ya erreur lors de la creation d'un user avec
            une email qui existe deja"""

        donnees = {
            'email': 'test@email.com',
            'password': 'mdpkjfj',
            'name': 'kiortest',
        }
        create_user(**donnees)
        res = self.client.post(CREATE_USER_URL, donnees)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_si_les_mots_se_pass_lege_sont_acceptes(self):
        """Test si erreur en cas de mot de passe faible """

        donnees = {
            'email': 'test@email.com',
            'password': '124',
            'name': 'kiortest',
        }
        res = self.client.post(CREATE_USER_URL, donnees)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # on veriffie que l'user n'a pas été enregistré
        user_enregistre_malges_le_pb = get_user_model().\
            objects.filter(email=donnees['email']).exists()
        self.assertFalse(user_enregistre_malges_le_pb)

    def test_creation_de_token_de_l_user(self):
        """Test la creation de token pour un user"""

        donnees_utilisateur = {
            "name": "tester",
            'email': "tes@tester.com",
            'password': "test-user-as555"
        }
        create_user(**donnees_utilisateur)
        res = self.client.post(TOKEN_URL, donnees_utilisateur)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_creation_de_token_avec_mauvais_identifiants(self):
        """Tester si erreur en cas de demande de token avec
        des mauvais identifiants """

        bonnes_donnees_utilisateur = {
            'email': 'levon@mail.com',
            'password': 'lebon mo de pass'
        }
        create_user(**bonnes_donnees_utilisateur)

        mauvaise_donnees_utilisateurs1 = {
            "email": '',
            "password": bonnes_donnees_utilisateur['email']}
        mauvaise_donnees_utilisateurs2 = {
            "email": bonnes_donnees_utilisateur['password'],
            "password": ''}

        mauvaise_requet1 = self.client.post(TOKEN_URL,
                                            mauvaise_donnees_utilisateurs1)
        mauvaise_requet2 = self.client.post(TOKEN_URL,
                                            mauvaise_donnees_utilisateurs2)

        self.assertNotIn('token', mauvaise_requet1.data)
        self.assertNotIn('token', mauvaise_requet2.data)

        self.assertEqual(
            mauvaise_requet1.status_code,
            status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            mauvaise_requet2.status_code,
            status.HTTP_400_BAD_REQUEST)

    def test_detail_sur_un_user_est_non_autorise(self):
        """
        Test si la recuperation de detaille sur un user
        retourne une erreur en cas de non authentifivation de l'user"""

        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTest(TestCase):
    """Les test qui ne consernent que les utilisatuers authentifiés"""

    def setUp(self):
        # creation et authentification de l'user de test
        self.user = create_user(
            email="test@exemple.com",
            password='le mot de pass',
            name='Non de Test'

        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_si_la_reccuperation_du_profil_est_un_secces(self):
        """Pour un user authentifié on veus veriffier que
        l'acces au profil est OK"""

        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data,
                         {
                            "name": self.user.name,
                            "email": self.user.email,
                         })

    def test_post_non_permis(self):
        """Test si les posts sont pas permis sur l'endpoint me"""

        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_mise_a_jour_du_profile(self):
        """Test si un utilisateur connecté peut mettre à jour ses infos"""

        nouvelles_donnes = {
            'name': "nouveau Nom",
            'password': "nouvea mot de pass"}

        res = self.client.patch(ME_URL, nouvelles_donnes)
        self.user.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertEqual(self.user.name, nouvelles_donnes['name'])
        self.assertTrue(self.user.check_password(nouvelles_donnes['password']))
