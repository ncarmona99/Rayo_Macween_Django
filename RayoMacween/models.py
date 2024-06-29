from django.db import models
import datetime

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Formulario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    appaterno = models.CharField(max_length=20)
    apmaterno = models.CharField(max_length=20)
    edad = models.IntegerField()
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    celular = models.CharField(max_length = 45)
    descripcion = models.CharField(max_length = 500)

    def __str__(self):
        return str(self.nombre) + " "+str(self.appaterno)
    
































































































class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self. apellido}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=100, default='', blank=True, null=True)
    imagen = models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField(default=1)
    telefono = models.CharField(max_length=10)
    fecha = models.DateField(default=datetime.datetime.today)
    estatus = models.BooleanField(default=False)

    def __str__(self):
        return self.producto
