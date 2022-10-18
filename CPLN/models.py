from email.policy import default
from tabnanny import verbose
from django.db import models
import datetime
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

alphabetical = RegexValidator(r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$', 'Solamente está permitido usar caracteres alfabéticos y un espacio entre palabras.')
numeric = RegexValidator(r'^[0-9]*$', 'Solamente está permitido usar caracteres numéricos.')
# Create your models here.

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=255)

    def __str__(self):
        return str(self.neighborhood)

class Candidate(models.Model):
    first_name = models.CharField(validators=[alphabetical, MinLengthValidator(3)], max_length=100, verbose_name="Nombre")
    last_name = models.CharField(validators=[alphabetical, MinLengthValidator(3)], max_length=100, verbose_name="Apellido")
    dateOfBirth = models.DateField(default=datetime.date.today, verbose_name="Fecha Nacimiento")
    email = models.EmailField(max_length=50, unique=True)
    telephone = models.CharField(validators=[numeric, MinLengthValidator(8)], max_length=20, verbose_name="Teléfono")
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, verbose_name="Barrio")
    STATUS = (
        ('P', 'Postulado'),
        ('R', 'Rechazado'),
        ('An', 'Analizando'),
        ('Ac', 'Aceptado'),
    )
    status = models.CharField(max_length=2, choices=STATUS, default='P', verbose_name="Estado")

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"
    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

class Volunteer(models.Model):
    first_name = models.CharField(max_length=100, validators=[alphabetical, MinLengthValidator(3)], verbose_name="Nombre")
    last_name = models.CharField(max_length=100, validators=[alphabetical, MinLengthValidator(3)], verbose_name="Apellido")
    dateOfBirth = models.DateField(default=datetime.date.today, verbose_name="Fecha Nacimiento")
    email = models.EmailField(max_length=50, unique=True)
    telephone = models.CharField(validators=[numeric, MinLengthValidator(8)], max_length=20, verbose_name="Teléfono")
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, verbose_name="Barrio")    
    class Meta:
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntarios"

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

class New(models.Model):
    title = models.CharField(max_length=100, default="Sin Título", verbose_name="Título")
    img = models.CharField(max_length=1000, verbose_name="Imágen")
    description = models.CharField(max_length=200, verbose_name="Descripción")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return str(self.title + ' ' + self.description)

class ListFood(models.Model):
    description = models.TextField(default="No hay peticiones específicas", verbose_name="Descripción")

    class Meta:
        verbose_name = "Lista de Alimentos"
        verbose_name_plural = "Lista de Alimentos"

    def __str__(self):
        return str(self.description)