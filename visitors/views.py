# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from visitors.models import Visitor
from visitors.forms import SearchForm


class VisitorListView(ListView):
    model = Visitor
    form_class = SearchForm
    context_object_name = 'visitor'
    template_name = 'visitor.html'

    def get_context_data(self, *args, **kwargs):
        context = super(VisitorListView, self).get_context_data(*args, **kwargs)

        phone_number = self.request.GET.get('phone_number')
        if phone_number:
            context.update({'phone_number': phone_number})

        context.update({'form': self.form_class()})

        return context

    def get_queryset(self):
        form = self.form_class(self.request.GET)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            return self.model.objects.filter(phone_number__icontains=phone_number)

        return []