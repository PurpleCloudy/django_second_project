from django.core.management.base import BaseCommand
from rating.models import Rating

class Command(BaseCommand):
    help = 'remove add entries from Rating Model'

    def handle(self, *args, **options):
        qset = Rating.objects.filter(text = 'created from command line')
        qset.delete()
        print(qset)