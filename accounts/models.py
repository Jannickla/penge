from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from penge import settings


class MyAccountManager(BaseUserManager):
    """
    Custom User Model, that allows you to log in via E-mail instead of username.

    NOTE! We're using username as NIP holder, so we did not remove it, but as NIP
    is harder to remember than e-mails, we've reserved it for that purpose, but done
    so e-mail is default login method. It's done for user experience sake!
    """
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('A user must have a valid email attached')
        if not username:
            raise ValueError('A user must have a valid username attached')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        is_admin = True
        is_staff = True
        is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    LANGUAGES = [
        ('en', 'English'),
        ('pl', 'Polish'),
        ('da', 'Danish'),
        ('se', 'Swedish'),
        ('no', 'Norwegian'),
    ]
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=45)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    language = models.CharField(default='en', choices=LANGUAGES, max_length=2)

    # Company Profile Fields
    co_logo = models.ImageField(upload_to="dashboard/logos", blank=True)
    co_slogan = models.CharField(max_length=150, default='No slogan')
    co_name = models.CharField(max_length=45)
    co_address = models.CharField(max_length=45)
    co_zip = models.CharField(max_length=45)
    co_city = models.CharField(max_length=45)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
