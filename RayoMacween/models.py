from django.db import models

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Formulario(models.Model):

    def get_default_genero():
        return Genero.objects.get_or_create(genero="Selecione su género")[0]

    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    appaterno = models.CharField(max_length=20)
    apmaterno = models.CharField(max_length=20)
    edad = models.IntegerField()
    id_genero = models.ForeignKey('Genero',default=get_default_genero,on_delete=models.CASCADE, db_column='idGenero')
    celular = models.CharField(max_length = 45)
    descripcion = models.CharField(max_length = 500)

    def __str__(self):
        return str(self.nombre) + " "+str(self.appaterno)