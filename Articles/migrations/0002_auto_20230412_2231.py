# Generated by Django 2.2 on 2023-04-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
