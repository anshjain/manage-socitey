# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from visitors.models import Visitor, VisitInfo


class VisitorAdmin(admin.ModelAdmin):
    pass


class VisitInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitInfo, VisitInfoAdmin)