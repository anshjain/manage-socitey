# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class SearchForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'autocomplete': 'off'}))