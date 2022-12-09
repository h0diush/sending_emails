from django.core.management.base import BaseCommand
from faker import Faker

from apps.users.models import User

fake = Faker()


class Command(BaseCommand):
    help = 'Создание пользователей для БД'

    def _get_create_user(self, username, email, first_name, last_name,
                         password, superuser: bool):
        if superuser:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='Количество пользователей')
        parser.add_argument('-a', '--admin', action='store_true',
                            help='Создание суперпользователя')

    def handle(self, *args, **options):
        qty = options['qty']
        admin = options['admin']
        for i in range(qty):
            username = fake.user_name()
            password = fake.password()
            email = fake.email()
            last_name = fake.last_name()
            first_name = fake.first_name()

            self._get_create_user(username, email, first_name, last_name,
                                  password, admin)
        return self.stdout.write(
            self.style.SUCCESS(f'Сгенерировано аккаунтов: {qty}'))
