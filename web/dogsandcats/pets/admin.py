# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pets


# Register your models here.

class PetsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pets, PetsAdmin)


