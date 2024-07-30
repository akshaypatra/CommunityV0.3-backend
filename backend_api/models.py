from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

# model for custom user
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


# model for profile  details for spicific user
class ProfileInfo(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bio=models.CharField(max_length=1000)
    skills=models.CharField(max_length=1000)
    work=models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


