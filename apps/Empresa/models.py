from django.db import models

# Create your models here.
class Sede(models.Model):
    sede = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return '%s'%(self.sede)