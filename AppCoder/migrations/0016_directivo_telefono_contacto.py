# Generated by Django 3.1.2 on 2022-02-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_auto_20220213_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='directivo',
            name='telefono_contacto',
            field=models.IntegerField(null=True),
        ),
    ]
