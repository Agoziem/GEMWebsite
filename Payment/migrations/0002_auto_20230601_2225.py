# Generated by Django 2.2 on 2023-06-01 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations_and_support',
            name='verified',
            field=models.BooleanField(),
        ),
    ]
