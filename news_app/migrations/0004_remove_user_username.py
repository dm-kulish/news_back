# Generated by Django 4.1.7 on 2023-03-14 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
