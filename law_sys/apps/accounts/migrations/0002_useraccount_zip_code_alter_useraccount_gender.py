# Generated by Django 5.1.3 on 2025-01-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='zip_code',
            field=models.CharField(blank=True, help_text='Zip Code', max_length=10, null=True, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Prefer not to say')], help_text='Gender', max_length=1, null=True, verbose_name='Gender'),
        ),
    ]
