# Generated by Django 5.1.1 on 2024-09-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahid', '0004_shahid_qr_code_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shahid',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]