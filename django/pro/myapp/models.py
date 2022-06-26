from django.db import models

# Create your models here.
class officeprofile (models.Model):
    profile = models.ImageField(blank=True, null=True, upload_to ='images')
    username = models.CharField(blank=False, null=False, max_length =100)

    def __str__(self):
        return str(self.username)