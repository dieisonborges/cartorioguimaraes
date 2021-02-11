from django.contrib import admin

from .models import Institutionals, Links, Services

# Register your models here.

admin.site.register(Links)
admin.site.register(Institutionals)
admin.site.register(Services)
