# Generated by Django 4.1.3 on 2023-02-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_alter_likes_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilePiture',
            field=models.ImageField(blank=True, default='default-profile-pic', upload_to='profile_pics/'),
        ),
    ]
