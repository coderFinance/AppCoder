# Generated by Django 3.1.2 on 2022-01-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_directivo_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='dni',
            field=models.IntegerField(null=True),
        ),
    ]
