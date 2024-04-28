"""
Test for the django admin modification.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    """Test for the Django Admin """

    def setUp(self):
        """Create User and Client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@ox.com",
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="emailex@gmail.com",
            password="jdd123",
            name='test_user'
        )

    def test_users_list(self):
        """Check users a listed on the list"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        """Check if the user creat page is avalable"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
