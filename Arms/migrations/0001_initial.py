# Generated by Django 2.2 on 2023-04-13 00:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arm_image', models.ImageField(upload_to='assests/Arms')),
                ('Arm', models.CharField(max_length=300)),
                ('sideline', models.CharField(max_length=300)),
                ('Vision', models.TextField(help_text='max of 400 words', max_length=400)),
                ('Mission', models.TextField(help_text='max of 400 words', max_length=400)),
                ('Organization_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Arms', to='Home.Organization_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Arm_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_beside', models.ImageField(upload_to='assests/Arms image beside')),
                ('heading', models.CharField(max_length=300)),
                ('sideline', models.CharField(max_length=300)),
                ('body', ckeditor.fields.RichTextField()),
                ('Arm_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Arms.Arm')),
            ],
        ),
    ]
