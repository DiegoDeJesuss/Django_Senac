from django.db import models

# Create your models here.

class comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    email         = models.EmailField()
    comentarios   = models.TextField()