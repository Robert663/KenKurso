# Generated by Django 4.0.6 on 2022-07-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='inscriptions',
            field=models.IntegerField(default=0),
        ),
    ]
