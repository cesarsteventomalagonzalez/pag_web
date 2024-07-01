from django.db import models
from core import settings
# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=40,verbose_name='Empresa',unique=True)
    contacto=models.CharField(max_length=10, blank=False,null=False)
    correo =  models.EmailField(max_length=100, blank=True, null=True, )
    logo = models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo= models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo1= models.FileField(upload_to='logo/empresa', blank=True, null=True)
    promo2= models.FileField(upload_to='logo/empresa', blank=True, null=True)



    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Empresa'
        ordering = ('nombre',)


    def get_image(self):
        if self.logo:
            return '{}{}'.format(settings.MEDIA_URL, self.logo)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.jpg')

    
    def get_promo(self):
        if self.promo:
            return '{}{}'.format(settings.MEDIA_URL, self.promo)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.jpg')

    
    def get_promo1(self):
        if self.promo1:
            return '{}{}'.format(settings.MEDIA_URL, self.promo1)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.jpg')

    
    def get_promo2(self):
        if self.promo2:
            return '{}{}'.format(settings.MEDIA_URL, self.promo2)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.jpg')
    


class Productos(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    foto = models.FileField(upload_to='logo/empresa', blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True, blank=False, null=False)
    numero_whatsapp = models.CharField(max_length=15, default='+593959682902') 

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return "{} - {}".format(self.codigo, self.nombre)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

        
        
        
     







    