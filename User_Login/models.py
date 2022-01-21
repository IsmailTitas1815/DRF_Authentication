from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.


class UserProfileManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone, gender, dob, username, access_code, **extra_fields):
        if not email:
            raise ValueError("User must have email!")
        if not password:
            raise ValueError("User must have password!")
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          phone=phone, gender=gender, dob = dob,  username=username, access_code=access_code, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email, password, first_name, last_name, phone, gender, dob, username, access_code, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, phone, gender, dob, username, access_code, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, phone, gender, dob, username, access_code, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, phone, gender, dob, username, access_code, **extra_fields)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
    ('Prefer Not To Say', 'Prefer Not To Say'),
)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=255, choices=GENDER, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    username = models.CharField(
        max_length=255, unique=True, null=False, blank=False)
    access_code = models.CharField(max_length=255, null=True, blank=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name',
                       'last_name', 'phone', 'gender', 'dob', 'access_code']

    def __str__(self):
        return self.email


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "ismailtitas1815@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
