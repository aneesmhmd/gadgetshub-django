# Generated by Django 4.1.7 on 2023-02-23 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_brand'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='category.brand'),
        ),
    ]
