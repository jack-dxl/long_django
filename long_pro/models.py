from django.db import models

# Create your models here.
import django.utils.timezone as timezone

class user_info(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    status = models.CharField(max_length=20, default=1)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, default=1)
    create_time = models.DateTimeField(default=timezone.now)
    old_login_time = models.DateTimeField(default=timezone.now)
    useing = models.CharField(max_length=20, default=1)
