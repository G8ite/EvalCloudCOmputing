# Generated by Django 5.0.6 on 2024-05-15 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_rename_original_name_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='original_name',
        ),
    ]
