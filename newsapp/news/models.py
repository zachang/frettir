from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    """Represents UserProfile model class"""

    def my_interests():
        # default value for users notification interests
        return {"interests": []}

    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    image = models.CharField(max_length=255, null=True)
    notifications = models.BooleanField(default=False)
    notify_interests = JSONField(default=my_interests)

    def __str__(self):  
          return "{}'s profile".format(self.user,)  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)

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