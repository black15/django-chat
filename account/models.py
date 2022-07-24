from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _

# Create your models here.
class AccountManager(BaseUserManager):
        def create_user(self, username, email, password, **other_fields):
                if not email:
                        raise ValueError('User must have an email')
                if not username:
                        raise ValueError('User must have a username')
                user = self.model(
                        email = self.normalize_email(email),
                        username = username,
                        **other_fields,
                )
                user.set_password(password)
                user.save()
                return user

        def create_superuser(self, username, email, password, **other_fields):
                
                other_fields.setdefault('is_staff', True)
                other_fields.setdefault('is_superuser', True)

                if other_fields.get('is_staff') is not True:
                        raise ValueError('is_staff must be True')
                if other_fields.get('is_superuser') is not True:
                        raise ValueError('is_superuser must be True')

                return self.create_user(username, email, password, **other_fields)

class Account(AbstractBaseUser, PermissionsMixin):

        email           = models.EmailField(max_length=50, verbose_name='Email', unique=True)
        username        = models.CharField(_("Username"), max_length=30, unique=True)
        bio             = models.TextField(_("Bio"), null=True, blank=True)
        date_joined     = models.DateTimeField(_("Date Joined"), auto_now_add=True)
        is_active       = models.BooleanField(_("is Active"), default=True)
        is_admin        = models.BooleanField(_("is Admin"), default=False)
        is_staff        = models.BooleanField(_("is Staff"), default=False)
        is_superuser    = models.BooleanField(_("is Superuser"), default=False)
        profile_img     = models.ImageField(_("Profile Image"), upload_to='profile_images/%y/%m/%d', max_length=200, default="profile_images/default.jpg", blank=True, null=True)
        hide_email      = models.BooleanField(_("Hide Email"), default=True, blank=True)

        friends         = models.ManyToManyField('Account', blank=True)

        objects = AccountManager()

        USERNAME_FIELD  = 'email'
        REQUIRED_FIELDS = ['username']

        def __str__(self):
                return self.username

class FriendRequest(models.Model):
        from_user       = models.ForeignKey(Account, related_name='from_user', on_delete=models.CASCADE)
        to_user         = models.ForeignKey(Account, related_name='to_user', on_delete=models.CASCADE)
        
        def __str__(self):
                return 'to ' + self.to_user.username