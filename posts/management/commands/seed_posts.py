import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):

    help = "this command create users"

    def add_arguments(self, parser):

        parser.add_argument(
            "--number", default=2, type=int, help="how many users want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            post_models.Post,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "number_of_people": lambda x: random.randint(1, 6)
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} posts created"))
