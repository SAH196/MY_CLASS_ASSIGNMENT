from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
import os

# Create your models here.

class signup(models.Model):
    mid = models.OneToOneField(User,on_delete=models.CASCADE)
    myprofile = models.ImageField(blank=True,null=True,upload_to ='images', default="/static/ge.jpg")


    def __str__(self):
        return str(self.mid)

def _delete_file(path):
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=signup)
def delete_file(sender, instance, *args, **kwargs):
    if instance.profile:
        _delete_file(instance.profile.path)
        print("Instance has deleted")


@receiver(pre_delete, sender=signup)
def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
    if instance.profile:
        _delete_file(instance.profile.path)
        print("In the process of deleting any instance")