# Generated by Django 3.2.4 on 2021-06-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_feedtable_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='store_photo_at',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='display_photo',
            field=models.ImageField(upload_to=models.CharField(max_length=200)),
        ),
    ]