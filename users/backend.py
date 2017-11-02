from core import settings
from .models import CustomUser
from django.contrib.auth.backends import ModelBackend 

class CustomBackend(ModelBackend):


    def authenticate(self, request, nickname=None):
        try:
            user = CustomUser.objects.get(nickname=nickname)
        except CustomUser.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = CustomUser(nickname=nickname)
            user.save()
        return user

    def get_user(self, nickname):
        try:
            return CustomUser.objects.get(nickname=nickname)
        except CustomUser.DoesNotExist:
            return None
