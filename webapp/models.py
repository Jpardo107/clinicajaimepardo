from django.db import models

class Paciente(models.Model):
    rut = models.CharField(max_length=9)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=30, null='true')
    telefono = models.IntegerField()
    email = models.CharField(max_length=30)
    fecNac = models.CharField(max_length=10)
    estCivil = models.CharField(max_length=20)
    comentario = models.TextField()

    def __str__(self):
        return f'Persona {self.id}: {self.rut} {self.nombres}'
