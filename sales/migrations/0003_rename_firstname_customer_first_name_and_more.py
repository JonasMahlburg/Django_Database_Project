# Generated by Django 5.2.1 on 2025-05-08 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_customer_newsletter_abo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
