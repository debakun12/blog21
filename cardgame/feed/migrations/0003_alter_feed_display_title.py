# Generated by Django 3.2.4 on 2021-06-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20210620_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='display_title',
            field=models.CharField(max_length=200),
        ),
    ]
