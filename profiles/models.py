from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # image = models.FileField(upload_to="images")   # It is considered bad practice to store "file" in database.It make it slow and blows the database also.Filefield will store the path of file in database and file will be stored in our hardisk.
    image = models.ImageField(upload_to="images")
