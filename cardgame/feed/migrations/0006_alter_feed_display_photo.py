# Generated by Django 3.2.4 on 2021-06-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_feed_display_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='display_photo',
            field=models.ImageField(upload_to=None),
        ),
    ]
