# Generated by Django 2.1.5 on 2020-09-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20200914_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
