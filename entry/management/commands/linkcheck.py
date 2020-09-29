from django.core.management.base import BaseCommand, CommandError
from entry.models import Entry

class Command( BaseCommand ):
    help = 'check entries for broken internal links'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle( self, *args, **options ):
        import re
        pattern = "\[[^]]+\]\(/([a-z0-9-]+)\)"
        self.stdout.write( "Checking {} entries".format( Entry.objects.count() ) )
        entries = set()
        links = set()
        for entry in Entry.objects.all():
            entries.add(entry.slug)
            for link in re.findall( pattern, entry.text ):
                links.add( link )

        self.stdout.write( "Internal links without entries:")
        self.stdout.write( str(links-entries) )
