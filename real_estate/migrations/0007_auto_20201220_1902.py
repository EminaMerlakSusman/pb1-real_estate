# Generated by Django 3.1.1 on 2020-12-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0006_auto_20201219_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='nu_rooms',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=1.0),
        ),
    ]
