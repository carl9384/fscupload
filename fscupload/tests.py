from django.test import TestCase,Client

from django.contrib.auth.models import User
# Create your tests here.

class CreateUserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser',email='cnegro@nysbc.org')
        user.set_password('testpassword')
        user.save()
        User.objects.create(username='temporary',password='temporary',email='cnegro@nysbc.org')
        self.client = Client()

    def test_user_info(self):
        testuser = User.objects.get(username='testuser')
        self.assertEqual(testuser.username,'testuser')
        self.assertEqual(testuser.email,'cnegro@nysbc.org')


    def test_login(self):
        response = self.client.login(username='testuser',password='testpassword')
        response_post = self.client.post('/accounts/login/',{'username':'testuser','password':'testpassword'})
        self.assertEqual(response,True)
        self.assertEqual(response_post.status_code,302)


