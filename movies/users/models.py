from django.db import models
from django.contrib.auth.models import AbstractUser

class theUser(AbstractUser):
  ROLES=[
    ('staff_1', 'Staff'),
    ('client_1', 'Client')
  ]

  role = models.CharField(max_length=20, choices=ROLES)

