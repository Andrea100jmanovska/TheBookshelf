# Generated by Django 4.2.2 on 2023-06-30 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]