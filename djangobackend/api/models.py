from django.db import models

# Create your models here.

class candidates(models.Model):
    canname = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    
