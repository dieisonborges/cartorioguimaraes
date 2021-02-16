from django.db import models
from django.utils.crypto import get_random_string

import os
import datetime

# Create your models here.

#Links
class Links(models.Model):
    """ Links """    
    #Columns
    link = models.TextField('Link')
    description = models.CharField('Descrição', max_length=200)

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
    name = models.CharField('Nome do Serviço', max_length=200)
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

#Arquivos
class CategoryArchives(models.Model):
    name = models.CharField('Categoria', max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    mother_category = models.ForeignKey('self', blank=True, null=True, related_name='category', on_delete=models.SET_NULL)
       
    #Default
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Categoria do Modelo"
        verbose_name_plural = "Categorias dos Modelos"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.name


class Archives(models.Model):

    def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = get_random_string(length=64) + datetime.datetime.now().strftime("%Y%m%d%H%M%S")  + "." + ext
        return os.path.join('archives', filename)

    category = models.ForeignKey(
        CategoryArchives, 
        on_delete=models.SET_NULL, 
        related_name='archives', 
        blank=True,
        null=True
    )

    docfile = models.FileField('Arquivo', upload_to=content_file_name)
    name = models.CharField(max_length=200)
    
    #Default
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Alterado em', auto_now=True)

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        ordering = ['id']

    #For DjangoAdmin
    def __str__(self):
        return self.name