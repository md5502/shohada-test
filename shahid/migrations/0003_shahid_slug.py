# Generated by Django 5.1.1 on 2024-09-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahid', '0002_alter_shahid_martyrdom_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shahid',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
