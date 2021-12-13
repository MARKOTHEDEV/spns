# Generated by Django 3.2 on 2021-12-13 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_peopledataforpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchInsightInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='spns_cover_image/')),
                ('heading', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='researchinsight_ParaGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('researchinsightinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.researchinsightinfo')),
            ],
        ),
    ]
