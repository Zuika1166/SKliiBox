# Generated by Django 3.2.12 on 2023-01-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0004_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='created_add',
        ),
    ]