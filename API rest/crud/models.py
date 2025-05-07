from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    apellido = models.CharField(max_length=100,verbose_name="Apellido")
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(verbose_name="Email")
    telefono = models.CharField(max_length=15,verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        db_table = 'persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['apellido', 'nombre']