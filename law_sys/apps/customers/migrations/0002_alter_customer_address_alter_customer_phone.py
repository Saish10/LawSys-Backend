# Generated by Django 5.1.3 on 2025-01-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, help_text='Customer address', null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, help_text='Customer phone number', max_length=15, null=True, verbose_name='Phone Number'),
        ),
    ]
