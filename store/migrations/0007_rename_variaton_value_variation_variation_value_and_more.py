# Generated by Django 4.1.7 on 2023-03-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='variaton_value',
            new_name='variation_value',
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('ram', 'ram'), ('storage', 'storage')], max_length=100),
        ),
    ]