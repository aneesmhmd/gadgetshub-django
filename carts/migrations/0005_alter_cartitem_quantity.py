# Generated by Django 4.1.6 on 2023-03-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
