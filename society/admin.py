# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from society.models import Society


class SocietyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Society, SocietyAdmin)