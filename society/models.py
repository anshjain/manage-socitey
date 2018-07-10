# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

POSITIONS = (
    ('Chairman', 'Chairman'),
    ('secretary', 'secretary'),
    ('treasurer', 'treasurer'),
)


class Society(models.Model):
    """
    Society information
    """
    name = models.CharField(max_length=255, verbose_name=_("Society Name"))
    contract_number = models.CharField(max_length=10, verbose_name=_("contact number"),
                                       blank=True, null=True, unique=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique= True)
    address = models.CharField(max_length=255, verbose_name=_("Society Location"))
    city = models.CharField(max_length=20, verbose_name=_("city"), default='Pune')
    state = models.CharField(max_length=20, verbose_name=_("state"), default='maharashtra')
    pin_code = models.CharField(max_length=6, verbose_name=_("pin code"), default='411021')
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=18.557024, verbose_name=_("latitude"))
    long = models.DecimalField(max_digits=9, decimal_places=6, default=73.75092, verbose_name=_("longitude"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Society")
        verbose_name_plural = _("Societies")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SocietyCommittee(models.Model):
    """
    Society Committee information
    """
    society = models.ForeignKey(Society, verbose_name=_('Society'), related_name='society_committee')
    member = models.OneToOneField('accounts.Member', verbose_name=_('Committee Member'),
                                  related_name='committee_member')
    position = models.CharField(max_length=9, choices=POSITIONS, default="Chairman")

    def __unicode__(self):
        return '{} {}'.format(self.member.name, self.position)

    def __str__(self):
        return '{} {}'.format(self.member.name, self.position)