from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password, **extra_fields):
        values = [email, name]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, **extra_fields)

    def create_author(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_author', True)
        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_author = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default=timezone.now)



    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]

    def get_bio(self):
        return self.bio

    def get_contact(self):
        return self.email + self.phone



#Generting authentication token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



















# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )

#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False) # a superuser
#     # notice the absence of a "Password field", that is built in.

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.

#     objects = UserManager()

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):              # __unicode__ on Python 2
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin


# #visitor model

# class Reader(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     name = models.CharField(max_length=50)   

#     def get_full_name(self):
#        # The user is identified by their email address
#        return self.email


# #author model

# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     name = models.CharField(max_length=50)    
#     bio = models.TextField()
#     contact = models.CharField(max_length=255)

#     def get_full_name(self):
#        # The user is identified by their email address
#        return self.email

#     def get_bio(self):
#         #Get user's bio
#         return self.bio
    
#     def get_contact(self):
#         #get user's contact information
#         return self.contact