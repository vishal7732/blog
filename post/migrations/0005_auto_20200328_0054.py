# Generated by Django 3.0.4 on 2020-03-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='alt',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='alt',
            field=models.CharField(max_length=50),
        ),
    ]