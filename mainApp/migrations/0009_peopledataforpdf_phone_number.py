# Generated by Django 3.2 on 2021-12-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopledataforpdf',
            name='phone_number',
            field=models.CharField(default='', max_length=100),
        ),
    ]
