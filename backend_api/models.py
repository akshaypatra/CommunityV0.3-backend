from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'college_name', 'state', 'city', 'enrollment_number', 'department', 'academic_year']

    def __str__(self):
        return self.email
