# Generated by Django 4.2.5 on 2023-10-30 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_uploadedimage_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to='unrecognized_faces/'),
        ),
    ]
