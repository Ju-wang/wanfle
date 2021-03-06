# Generated by Django 3.2.8 on 2021-11-13 06:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20211112_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='OttType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.otttype'),
        ),
        migrations.AlterField(
            model_name='post',
            name='explain',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_of_people',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
