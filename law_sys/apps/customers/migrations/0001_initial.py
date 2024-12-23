# Generated by Django 5.1.3 on 2024-12-23 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(help_text='Customer name', max_length=255, verbose_name='Customer Name')),
                ('email', models.EmailField(db_index=True, help_text='Enter a valid email address (e.g., example@domain.com).', max_length=254, unique=True, verbose_name='Email Address')),
                ('phone', models.CharField(blank=True, help_text='Customer phone number', max_length=15, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, help_text='Customer address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='customers.customer')),
            ],
            options={
                'verbose_name': 'Customer Domain',
                'verbose_name_plural': 'Customer Domains',
                'db_table': 'customer_domains',
            },
        ),
    ]