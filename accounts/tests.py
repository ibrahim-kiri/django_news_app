from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
                username="testuser",
                email="testuser@example.com",
                password="testpass1234",
                )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
                username="admin",
                email="ibrahimkiri.stitch@gmail.com",
                password="admin",
                )
        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.email, "ibrahimkiri.stitch@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
