# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
class Pets(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
