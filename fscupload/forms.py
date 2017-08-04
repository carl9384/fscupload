from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User

class CustomUserForm(RegistrationFormUniqueEmail):

    class Meta:
            model = User
            fields = ['username','email','password1','password2']
