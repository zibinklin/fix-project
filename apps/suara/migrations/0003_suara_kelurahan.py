# Generated by Django 2.1.7 on 2019-04-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kelurahan', '0001_initial'),
        ('suara', '0002_suara_create_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='suara',
            name='kelurahan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kelurahan.Kelurahan'),
        ),
    ]