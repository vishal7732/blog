# Generated by Django 3.0.4 on 2020-03-27 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200328_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='alt',
            new_name='alt_profile',
        ),
    ]
