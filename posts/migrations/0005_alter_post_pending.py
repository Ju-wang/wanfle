# Generated by Django 3.2.8 on 2021-11-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pending',
            field=models.CharField(choices=[('모집중', '모집중'), ('모집완료', '모집완료')], default='모집중', max_length=5),
        ),
    ]
