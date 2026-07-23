from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a new user programmatically with a hashed password."

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, required=True, help="Username for the new user")
        parser.add_argument("--email", type=str, required=True, help="Email address")
        parser.add_argument("--password", type=str, required=True, help="Password for the user")
        parser.add_argument("--admin", action="store_true", help="Create as a superuser/admin")

    def handle(self, *args, **options):
        username = options["username"]
        email = options["email"]
        password = options["password"]
        is_admin = options["admin"]

        if User.objects.filter(username=username).exists():
            raise CommandError(f'User with username "{username}" already exists.')

        if is_admin:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created SUPERUSER "{user.username}"')
            )
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created USER "{user.username}"')
            )