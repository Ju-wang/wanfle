# Generated by Django 3.2.8 on 2021-10-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pending',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
