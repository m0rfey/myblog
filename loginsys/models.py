from django.contrib.auth.models import User, UserManager
from django.db import models

class UserProfile(User):
    users_id = models.ForeignKey(User)
    phone = models.CharField(max_length=13, blank=False)

    objects = UserManager()
