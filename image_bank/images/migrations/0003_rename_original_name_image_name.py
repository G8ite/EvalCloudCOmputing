# Generated by Django 5.0.6 on 2024-05-15 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='original_name',
            new_name='name',
        ),
    ]