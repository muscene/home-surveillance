# Generated by Django 4.2.5 on 2023-10-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_profile_images/'),
        ),
    ]
