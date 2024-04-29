"""
Test for the user Api
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
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public feature of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_user_success(self):
        """Tes creatin a user is successful"""

        payload = {
            'email': 'test@examole.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exits_error(self):
        """Test error returned if user with email exist."""

        payload = {
            'email': 'test@examole.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_errors(self):
        """Test an error is returned when password les than 5 chars."""

        payload = {
            'email': 'test@examole.com',
            'password': 'plo',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)

    def test_create_token_for_use(self):
        """ Test generates token for valid Credentianss"""

        user_details = {
            'name': "Test Name",
            'email': 'test@example.com',
            'password': 'test-user-password123',

        }
        create_user(**user_details)
        payload = {
            'email': user_details['email'],
            'password': user_details['password']
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test returns error if credentians invalid"""

        create_user(email='test@example.com', password="badpass")

        payload = {
            'email': 'test@example.com',
            'password': 'test-user-password123',

        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_with_blank_password(self):
        """Test posting a blank password return an error """

        payload = {
            'email': 'test@example.com',
            'password': '',
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateUserApiTest(TestCase):
    """Test API request that require authentication."""

    def setUp(self):
        self.user = create_user(
            email='test@example.com',
            password='estpass123',
            name='Test Name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""

        res = self.client.get(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'name': self.user.name,
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        """Test POST is not allowed for me Endpoint"""

        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """The for updatin profile for the authenticated user"""

        playload = {'name': 'new name', 'password': "new password" }
        res = self.client.patch(ME_URL, playload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, playload['name'] )
        self.assertTrue(self.user.check_password(playload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
