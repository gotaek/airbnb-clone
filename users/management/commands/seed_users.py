from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review


class Command(BaseCommand):

    help = "This command creates many users"

    # arguments를 설정할 수 있음
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do you want to create?",
        )

    #
    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(
            User, number, {"is_staff": False, "is_superuser": False}
        )  # model argument custom
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Users created!"))