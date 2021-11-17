from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "this command create users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help="how many users want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))
