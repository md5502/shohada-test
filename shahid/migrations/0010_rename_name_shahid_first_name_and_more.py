# Generated by Django 5.1.1 on 2024-09-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shahid', '0009_alter_image_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shahid',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='shahid',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='shahid',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shahid',
            name='birth_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shahid',
            name='important_quotes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shahid',
            name='will',
            field=models.TextField(blank=True, null=True),
        ),
    ]
