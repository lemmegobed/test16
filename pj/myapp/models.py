from django.db import models

# Create your models here.
class course(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=10)