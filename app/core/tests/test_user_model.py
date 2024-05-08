"""
Les tests relatifs au models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test des Models"""

    def test_la_creation_d_un_utilisateu_grace_a_son_email_passe(self):
        """Test pour verifier si la creation d'un user \
            grace a son Email fonctionne"""
        email = "tes@example.com"
        password = 'tesspasswor'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_si_l_email_a_ete_normalisee(self):
        """Test si l'email de l'user est normalisaliséé"""

        exemples_d_emails = [
            ['test1@EXeMPLE.com', 'test1@exemple.com'],
            ['Test2@Exemple.com', 'Test2@exemple.com'],
            ['TEST3@EXEMPLE.COM', 'TEST3@exemple.com'],
            ['test4@exemple.COM', 'test4@exemple.com']
            ]

        for email, attendue in exemples_d_emails:
            user = get_user_model().objects.create_user(email, 'pass')
            self.assertEqual(user.email, attendue)

    def test_si_la_creation_d_un_user_sans_email_raise_an_error(self):
        """
            Test si on a belle et bien une exception lors de la creation d'un
            d'un user sans Email ou avec une Email invalide
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass')

    def test_la_creation_des_super_utilisateur(self):
        """Test si on peut belle et bien creer une ***SUPERUSER*** """

        user = get_user_model().objects.create_superuser(
            'teste@exemple',
            'passs'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
