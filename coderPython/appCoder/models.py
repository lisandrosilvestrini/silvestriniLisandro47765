from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):

    def __str__(self) -> str:
        return f"id: {self.id}, title: {self.title}"
    
    # atributos
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateField()
    condition = models.CharField(max_length=100, default="usado")

class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Categ(models.Model):

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}"
    
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Categoria(models.Model):
    pass
class Tecnologia(models.Model):
    pass
class Muebles(models.Model):
    pass
class Cocina(models.Model):
    pass
class Decoracion(models.Model):
    pass
