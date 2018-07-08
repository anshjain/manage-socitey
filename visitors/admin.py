# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from visitors.models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Visitor, VisitorAdmin)