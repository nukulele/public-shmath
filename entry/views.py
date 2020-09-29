from django.conf import settings
from django.views.generic import DetailView

from .models import Entry


class EntryDetailView( DetailView ):
    model = Entry
    template_name = "entry/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs )
        context['show_edit_links'] = settings.SHOW_EDIT_LINKS
        return context

