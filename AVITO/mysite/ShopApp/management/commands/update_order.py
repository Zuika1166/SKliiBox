from django.core.management import BaseCommand
from ShopApp.models import Order, Product
from django.contrib.auth.models import User



class Command(BaseCommand):
    def handle(self, *args,**options):

        order = Order.objects.first()
        products = Product.objects.all()

        if not order:
            self.stdout.write('No order found')
            return

        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Saved all Order {order.products.all()} to order {order}'
            )
            
            
        
        )