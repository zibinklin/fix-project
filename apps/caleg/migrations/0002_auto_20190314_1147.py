# Generated by Django 2.1.5 on 2019-03-14 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caleg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caleg',
            name='dapil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calegs', to='dapil.Dapil'),
        ),
    ]
