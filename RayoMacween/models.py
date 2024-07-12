from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Formulario(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    )

    def get_default_genero():
        return Genero.objects.get_or_create(genero="Seleccione su género")[0]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios')
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    appaterno = models.CharField(max_length=20)
    apmaterno = models.CharField(max_length=20)
    edad = models.IntegerField()
    id_genero = models.ForeignKey('Genero', default=get_default_genero, on_delete=models.CASCADE, db_column='idGenero')
    celular = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.nombre} {self.appaterno}"
