from django.db import models
from django.contrib.auth.models import User, update_last_login
from django.db.models.deletion import CASCADE


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username