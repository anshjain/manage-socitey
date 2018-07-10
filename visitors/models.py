# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Visitor(models.Model):
    """
    Visitor information
    """
    name = models.CharField(max_length=255, verbose_name=_("Visitor Name"))
    phone_number = models.CharField(max_length=10, verbose_name=_("Phone number"))
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    address = models.CharField(max_length=255, verbose_name=_("Visitor address"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))

    class Meta:
        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class VisitInfo(models.Model):
    """
    Visitor visit information
    """
    society = models.ForeignKey('society.Society', verbose_name=_('society'), related_name='visitor_society')
    flat_number = models.ForeignKey('accounts.FlatDetail', verbose_name=_('flat_number'), related_name='visit_flat')
    visitor = models.ForeignKey(Visitor, verbose_name=_('Visitor'))
    number_of_visitor = models.CharField(max_length=2, verbose_name=_("No. Of Visitor"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    check_in = models.DateTimeField(auto_now_add=True, verbose_name=_("Check In Time"))
    check_out = models.DateTimeField(verbose_name=_("Check out Time"), blank=True, null=True)

    class Meta:
        verbose_name = _("Visit Info")
        verbose_name_plural = _("Visit Info")

    def __unicode__(self):
        return "{}-{}".format(self.visitor.name, self.flat_number)

    def __str__(self):
        return "{}-{}".format(self.visitor.name, self.flat_number)