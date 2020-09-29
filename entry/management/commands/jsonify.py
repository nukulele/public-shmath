from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command( BaseCommand ):
    help = 'exports the entry database as JSON'

    def handle( self, *args, **options ):
        call_command('dumpdata', 'entry', indent=2)

