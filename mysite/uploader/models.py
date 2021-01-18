from django.db import models

# Create your models here.
class Upload(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.FileField()
