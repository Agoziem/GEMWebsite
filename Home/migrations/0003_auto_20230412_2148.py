# Generated by Django 2.2 on 2023-04-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20230412_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='facebook',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='staff',
            name='instagram',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='staff',
            name='twitter',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='staff',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
