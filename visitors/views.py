# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView


from accounts.models import FlatDetail
from society.models import Society
from visitors.models import Visitor, VisitInfo
from visitors.forms import SearchForm, VisitorForm


class VisitorListView(ListView):
    model = VisitInfo
    form_class = SearchForm
    context_object_name = 'visitorinfo'
    template_name = 'visitor_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(VisitorListView, self).get_context_data(*args, **kwargs)

        context.update({'form': self.form_class(self.request.GET)})
        return context

    def get_queryset(self):
        form = self.form_class(self.request.GET)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            return self.model.objects.filter(visitor__phone_number__icontains=phone_number)

        return self.model.objects.filter(check_out__isnull=True)


#@method_decorator(login_required, name='dispatch')
class CreateVisitorView(FormView):
    form_class = VisitorForm
    model = VisitInfo
    template_name = 'visitor_entry.html'
    success_url = '/'

    def form_valid(self, form):
        # check account present with phone number or not.
        visitor, created = Visitor.objects.get_or_create(
            phone_number=form.cleaned_data['phone_number'],
        )
        if created:
            visitor.name = form.cleaned_data['name']
            visitor.email = form.cleaned_data['email']
            visitor.address = form.cleaned_data['address']
            visitor.save()

        # hard code as of now
        society = Society.objects.all().first()

        no_of_visitor = form.cleaned_data['no_of_visitor']

        _, record_created = self.model.objects.get_or_create(
            society=society,
            flat_number=FlatDetail.objects.filter(flat_number=form.cleaned_data['flat_number']).first(),
            visitor=visitor,
            number_of_visitor=no_of_visitor,
            check_in=datetime.now()
        )

        return super(CreateVisitorView, self).form_valid(form)
