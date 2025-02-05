# Generated by Django 5.1.1 on 2024-09-27 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahid', '0006_alter_shahid_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shahid',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shohada_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shahid.shahid')),
            ],
        ),
    ]
