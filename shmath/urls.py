"""shmath URL Configuration


"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView, TemplateView

from graphene_django.views import GraphQLView

from entry.views import EntryDetailView

urlpatterns = []

# if it's a read-only system, don't even show the admin paths
if settings.SHOW_EDIT_LINKS:
    urlpatterns = [
      path( 'admin/', admin.site.urls ),
    ]

urlpatterns += [
    path( '', RedirectView.as_view( url=reverse_lazy( "entry-detail", args=[ 'home', ] ) ) ),
    path( 'scratch/', TemplateView.as_view( template_name="entry/scratch_edit.html" ), name='scratch-edit' ),
    path( 'graphql', csrf_exempt( GraphQLView.as_view( graphiql=True ) ) ),
    path( 'tags/<int:page>/', TemplateView.as_view( template_name="entry/tag_list.html" ) ),
    path( 'entries/<int:page>/', TemplateView.as_view( template_name="entry/entry_list.html" ) ),
    path( 'entries/<slug:slug>/<int:page>/', TemplateView.as_view( template_name="entry/entry_tag_list.html" ) ),
    path( '<slug:slug>/', EntryDetailView.as_view(), name="entry-detail" ),
]

