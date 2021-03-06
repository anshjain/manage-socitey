"""manage_society URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, static
from django.contrib import admin

from django.views.generic import TemplateView
from visitors.views import VisitorListView, CreateVisitorView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', VisitorListView.as_view(template_name='visitor_list.html'), name='home'),
    url(r'^search/$', VisitorListView.as_view(), name='search-visitor'),
    url(r'^add/$', CreateVisitorView.as_view(), name='add-visitor'),
    url(r'^about/$', TemplateView.as_view(template_name="about_us.html"), name='about'),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
