# Generated by Django 4.2 on 2023-05-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
