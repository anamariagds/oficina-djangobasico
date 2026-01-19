from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    
    def __str__(self):
        return self.titulo
