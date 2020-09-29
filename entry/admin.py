from django.contrib import admin
from .models import Entry, Tag

admin.site.register( Tag )


@admin.register( Entry )
class EntryAdmin( admin.ModelAdmin ):
    filter_horizontal = ('tags',)
    list_display = ('slug', 'name', 'date_edit')
    search_fields = ('slug',)
