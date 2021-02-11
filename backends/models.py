from django.db import models

# Create your models here.

#Links
class Links(models.Model):
    """ Links """    
    #Columns
    link = models.TextField('Link')
    description = models.TextField('Descrição')

    #Default
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Link Útil"
        verbose_name_plural = "Links Úteis"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.description

#Services
class Services(models.Model):
    """ Services """    
    #Columns
    name = models.TextField('Nome do Serviço')
    description = models.TextField('Descrição')
    slug = models.CharField('Slug', max_length=200)

    #Default
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.description

#Institutional
class Institutionals(models.Model):
    """ Institutional """    
    #Columns
    name = models.TextField('Nome')
    description = models.TextField('Descrição')
    slug = models.CharField('Slug', max_length=200)

    #Default
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Institucional"
        verbose_name_plural = "Institucionais"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.description
