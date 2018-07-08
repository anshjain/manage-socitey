# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


FLAT_STATUS = (
    ('Owned', 'Owned'),
    ('Rented', 'Rented'),
    ('Empty', 'Empty')
)


class UserProfile(models.Model):
    """
    User profile which will associate with Society
    """
    user = models.OneToOneField(User, blank=True, null=True)
    society = models.ForeignKey('society.Society', verbose_name=_('society'), related_name='user_society')

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username


class MemberType(models.Model):
    """
    Member types owner or Tenant
    """
    name = models.CharField(max_length=50, verbose_name=_("name"))

    class Meta:
        verbose_name = _("Member type")
        verbose_name_plural = _("Member types")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    Member info.
    """
    name = models.CharField(max_length=255, verbose_name=_("Member Name"))
    phone_number = models.CharField(max_length=10, verbose_name=_("phone number"))
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    type = models.ForeignKey(MemberType, verbose_name=_('type'), related_name='membertypes')

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class FlatDetail(models.Model):
    """
    Flat details
    """
    society = models.ForeignKey('society.Society', verbose_name=_('society'), related_name='flat_society')
    flat_number = models.CharField(max_length=255, verbose_name=_("Flat Number"))
    owner = models.ForeignKey(Member, verbose_name=_('owner'), related_name='owners')
    status = models.CharField(max_length=9, choices=FLAT_STATUS, default="Owned")
    tenant = models.ForeignKey(Member, verbose_name=_('tenant'), related_name='tenants', null=True, blank=True)

    class Meta:
        verbose_name = _("Flat Detail")
        verbose_name_plural = _("Flat Details")

    def __unicode__(self):
        return "{}-{}".format(self.flat_number, self.society.name)

    def __str__(self):
        return "{}-{}".format(self.flat_number, self.society.name)