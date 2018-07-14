# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class SearchForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Phone Number', 'autocomplete': 'off',
            'class': 'w3-input w3-border',
    }))


class VisitorForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border',
                                                         'placeholder': 'Visitor Name'})
    )

    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', max_length=10,
                                    widget=forms.NumberInput(
                                        attrs={'placeholder': 'Phone Number',
                                               'autocomplete': 'off', 'class': 'w3-input w3-border',
                                               'onkeyup': "javascript:get_description();"}
                                    ),
                                    error_messages={
                                        'required': "Phone number must be entered in the format: '9999999999'"
                                    })

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'autocomplete': 'off', 'class': 'w3-input w3-border'}
    ))

    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Address', 'autocomplete': 'off',
                                                           'class': 'w3-input w3-border', 'rows': '4'}))

    flat_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border',
                                                                'placeholder': 'Whom you want to meet, flat Number ?'})
    )

    no_of_visitor = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Number of Visitors',
                                                                    'autocomplete': 'off',
                                                                    'class': 'w3-input w3-border'}))