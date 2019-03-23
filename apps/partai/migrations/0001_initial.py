# Generated by Django 2.1.5 on 2019-03-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no_urut', models.IntegerField(blank=True, null=True)),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='upload_pict/')),
            ],
        ),
    ]
