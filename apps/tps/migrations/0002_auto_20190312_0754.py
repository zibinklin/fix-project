# Generated by Django 2.1.5 on 2019-03-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tps',
            old_name='lingkungan',
            new_name='address',
        ),
    ]
