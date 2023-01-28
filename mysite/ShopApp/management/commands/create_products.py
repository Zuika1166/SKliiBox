from django.core.management import BaseCommand
from ShopApp.models import Product

class Command(BaseCommand):
    

    def handle(self, *args,**options):
        self.stdout.write('Create products')

        products_names = [
            'LapTop',
            'DeskTOp',
            'SmartPHONE',
        ]

        for products_name in products_names:
            product, created_at = Product.objects.get_or_create(name=products_name)
            self.stdout.write(f'Created Product {product.name}')


        self.stdout.write(self.style.SUCCESS('Products created'))

