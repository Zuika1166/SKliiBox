from django.core.management import BaseCommand
from ShopApp.models import Order
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args,**options):
        self.stdout.write('Create Order')

        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address = 'USA, Los-Angeles',
            promocode = 'U2023SA',
            user = user,
        )

        self.stdout.write(f'Created Order {order}')