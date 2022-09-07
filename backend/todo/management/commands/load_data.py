from django.core.management import BaseCommand
from todo.models import Todo

class Command(BaseCommand):
    help = 'loads data into database if needed'

    def handle(self, *args, **options):
        if Todo.objects.count() == 0:
            Todo.objects.create(
                title = "Sample Title"
            )