from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manages the object update to the database"""

    def create_user(self, email, name, password=None):
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a superuser with given email, name and pasword"""
        user = self.create_user(email, name, password)
        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User Profile Database to store the user data"""
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """returns full name with space inbetween"""
        return self.name

    def get_short_name(self):
        """returns the first name """
        return self.name

    def __str__(self):
        """sting representation of the object"""
        return self.email


class ProfileFeedItem(models.Model):
    """Database for the status update of each user"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text


