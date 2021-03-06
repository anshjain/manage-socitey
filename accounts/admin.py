# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.models import UserProfile, Member, FlatDetail


class UserProfileAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


class FlatDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(FlatDetail, FlatDetailAdmin)