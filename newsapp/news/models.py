from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):
        """
        Creates and saves a User with the given email, first_name,
        last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, password):
        """
        Creates and saves a superuser with the given email, 
        last_name, first_name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Represents User model class"""

    username =  models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    image = models.CharField(max_length=255, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        # returns all admins
        return self.is_admin


class Category(models.Model):
    """Represents Category model class"""

    category_name = models.CharField(max_length=255)


class News(models.Model):
    """Represents News model class"""

    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


class Comment(models.Model):
    """Represents Comments model class"""

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)