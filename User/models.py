from django.db import models
import uuid
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.shortcuts import reverse

# Create your models here


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username=None, password=None):

        if not email:
            raise ValueError("must have user email")
        if not username:
            username = email.split("@")[0]
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email), username=username, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    object = UserManager()

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER = (
        (GENDER_MALE, ("Male")),
        (GENDER_FEMALE, ("Female")),
        (GENDER_OTHER, ("Other")),
    )

    username = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(("gender"), choices=GENDER, max_length=10, blank=True)
    password = models.CharField(max_length=20)
    tel = models.CharField(max_length=11, null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    pro = models.BooleanField(default=False, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    """email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)"""

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User:profile", kwargs={"pk": self.pk})


"""def verift_email(self):
    if self.email_verified is False:
        secret = uuid.uuid4().hex[:20]
        self.email_secret = secret
        send_mail("Verify Jaebin Account", "Verify Account",  )
    return """
