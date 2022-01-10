from datetime import timedelta, date
from random import randint, choice

from django.core.management import BaseCommand
from django.db.utils import IntegrityError

from users.models import Users, UserProfiles


class Command(BaseCommand):
    help = 'Создание случайных пользователей'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')
        parser.add_argument('-p', '--prefix', type=str, help='Префикс для username и email')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']

        users = list(self.generate_users(prefix, total))

        for user in users:
            try:
                user.save()
            except IntegrityError:
                print('User already exists')
            else:
                u_p = UserProfiles.objects.filter(user=user)
                u_p.update(**self.set_user_in_profiles())

    @staticmethod
    def generate_users(prefix, total):
        return (Users(
            email='{}{}@mail.ru'.format(prefix, i),
            username='{}{}'.format(prefix, i),
            birthday=str(date.today() - timedelta(weeks=randint(18, 40) * 51, days=randint(1, 30))),
            password=f'AASSSS42',
            first_name='{}'.format(prefix),
            last_name='{}'.format(i)
        )
            for i in range(total))

    @staticmethod
    def set_user_in_profiles():
        return {
                'gender': choice(['Male', 'Female']),
                'region': choice(['Russia', 'English']),
                'phone': f'+{choice((1,7, 8))}'+''.join([str(randint(1, 10)) for _ in range(10)])}
