from django.contrib import admin

from .models import Archives, Institutionals, Links, Services, CategoryArchives

from django import forms


# Register your models here.


admin.site.register(Archives)
admin.site.register(CategoryArchives)
admin.site.register(Links)
admin.site.register(Institutionals)
admin.site.register(Services)
