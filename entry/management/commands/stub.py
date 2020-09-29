from django.core.management.base import BaseCommand, CommandError
from entry.models import Entry, Tag


class Command( BaseCommand ):
    help = 'creates a stub entry'

    def add_arguments( self, parser ):
        parser.add_argument( 'name', type=str )

    def handle( self, *args, **options ):
        # self.stdout.write( options['name'] )
        t = Entry( name=options[ 'name' ] )
        t.text = "*This is a stub entry. Add vast knowledge here.*"
        t.clean()
        t.save()
        t.tags.add( Tag.objects.get( slug='stub' ) )
        self.stdout.write( "Created stub article '{}'".format( options[ 'name' ] ) )
