# Generated by Django 2.2 on 2023-06-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_event_gem_arm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='GEM_Arm',
            field=models.CharField(choices=[('Bible Studies', 'Bible Studies'), ('Revival Prayers', 'Revival Prayers'), ('Foundation', 'Foundation'), ('Women’s Hub', 'Women’s Hub'), ('Partners', 'Partners')], default='None', max_length=300),
        ),
    ]
