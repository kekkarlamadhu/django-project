# Generated by Django 3.0.4 on 2020-04-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_userdata_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='profile_image',
            field=models.ImageField(blank=True, default='logo6.png', null=True, upload_to='users/'),
        ),
    ]
