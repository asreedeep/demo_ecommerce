# Generated by Django 5.0.1 on 2024-02-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_order_delivery_status_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(),
        ),
    ]
