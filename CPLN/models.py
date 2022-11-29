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

    class Meta:
        verbose_name = "Barrio"
        verbose_name_plural = "Barrios"

    def __str__(self):
        return str(self.neighborhood)

class CandidateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status=Candidate.ACEPTED)

class Candidate(models.Model):
    POSTULATED = 'P'
    REJECTED = 'R'
    ANALISING = 'An'
    ACEPTED = 'Ac'

    first_name = models.CharField(validators=[alphabetical, MinLengthValidator(3)], max_length=100, verbose_name="Nombre")
    last_name = models.CharField(validators=[alphabetical, MinLengthValidator(3)], max_length=100, verbose_name="Apellido")
    dateOfBirth = models.DateField(default=datetime.date.today, verbose_name="Fecha Nacimiento", null=True)
    email = models.EmailField(max_length=50, unique=True)
    telephone = models.CharField(validators=[numeric, MinLengthValidator(8)], max_length=20, verbose_name="Teléfono")
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, verbose_name="Barrio")
    STATUS = (
        (POSTULATED, 'Postulado'),
        (REJECTED, 'Rechazado'),
        (ANALISING, 'Analizando'),
        (ACEPTED, 'Aceptado'),
    )
    status = models.CharField(max_length=2, choices=STATUS, default='P', verbose_name="Estado")


    objects = CandidateManager()
    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"
    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

class VolunteerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Candidate.ACEPTED)


class Volunteer(Candidate):
    objects = VolunteerManager()
    class Meta:
        proxy = True
        verbose_name = "Voluntario"
        verbose_name_plural = "Voluntarios"

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


class Origin(models.Model):
    description = models.CharField(max_length=40, default="Sin orígen", verbose_name="Descripción")

    class Meta:
        verbose_name = "Orígen"
        verbose_name_plural = "Orígenes"

    def __str__(self):
        return str(self.description)

class MonetaryDonation(models.Model):
    amount = models.IntegerField(verbose_name="Monto")
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, verbose_name="Orígen")

    class Meta:
        verbose_name = "Donación monetaria"
        verbose_name_plural = "Donaciones monetarias"

    def __str__(self):
        return str(self.amount)

class Donation(models.Model):
    donator = models.CharField(max_length=40, default="Anónimo", verbose_name="Donante")
    date = models.DateField(null=True, verbose_name="Fecha de donación")

    class Meta:
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"

    def __str__(self):
        return str(self.donator)

class MonetaryDonation(models.Model):
    amount = models.IntegerField(verbose_name="Monto")
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, verbose_name="Orígen")
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True, verbose_name="Donación")

    class Meta:
        verbose_name = "Donación monetaria"
        verbose_name_plural = "Donaciones monetarias"

    def __str__(self):
        return str(self.amount)

class ProductType(models.Model):
    description = models.CharField(max_length=40, null=False, verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de producto"
        verbose_name_plural = "Tipos de productos"

    def __str__(self):
        return str(self.description)

class Product(models.Model):
    KILOGRAMS = 'kg'
    GRAMS = 'gr'
    MILLILITERS = 'ml'
    LITERS = 'lt'
    UNITS = 'U'

    description = models.CharField(max_length=40, null=False, verbose_name="Descripción")
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name="Tipo de producto")
    UNITTYPE = (
        (KILOGRAMS, 'Kilogramos'),
        (GRAMS, 'Gramos'),
        (MILLILITERS, 'Mililitros'),
        (LITERS, 'Litros'),
        (UNITS, 'Unidades'),
    )
    unit_type = models.CharField(max_length=2, choices=UNITTYPE, default='U', verbose_name="Tipo de unidad")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return str(self.description)

class ProductDonation(models.Model):
    quantity = models.IntegerField(verbose_name="Cantidad")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, verbose_name="Donación")

    class Meta:
        verbose_name = "Donación de productos"
        verbose_name_plural = "Donaciones de productos"

    def __str__(self):
        return str(self.product + ' ' + self.quantity)

class Lunch(models.Model):
    description = models.CharField(max_length=40, null=False, verbose_name="Descripción")

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"

    def __str__(self):
        return str(self.description)

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    lunch = models.ForeignKey(Lunch, related_name = 'ingredients', on_delete=models.CASCADE, verbose_name="Almuerzo")
    quantity = models.IntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return f'{self.product.description}'

class Family(models.Model):
    name = models.CharField(max_length=40, null=False, verbose_name="Nombre")

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

    def __str__(self):
        return str(self.name)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, verbose_name="Familia")
    quantity = models.IntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventario"

    def __str__(self):
        return f'{self.product.description, self.quantity}'

class Role(models.Model):
    role = models.CharField(max_length=40, null=False, verbose_name="Rol")
    description = models.CharField(max_length=40, default=" ", verbose_name="Descripción")

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return str(self.role)

class FamilyVolunteer(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, verbose_name="Voluntario")
    family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name="Familia")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Rol")

    class Meta:
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"

    def __str__(self):
        return str(self.family + ' ' + self.volunteer)

class Withdrawal(models.Model):
    familygiver = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='dadora', verbose_name="Familia dadora")
    familyreciever = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='receptora', verbose_name="Familia receptora")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de retiro")

    class Meta:
        verbose_name = "Retiro"
        verbose_name_plural = "Retiros"

    def __str__(self):
        return str(self.familygiver + '-' + self.familyreciever)

class WithdrawalDetail(models.Model):
    withdrawal = models.ForeignKey(Withdrawal, on_delete=models.CASCADE, verbose_name="Retiro")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    quantity = models.IntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name = "Detalle del retiro"
        verbose_name_plural = "Detalle de los retiros"

    def __str__(self):
        return str(self.withdrawal)
