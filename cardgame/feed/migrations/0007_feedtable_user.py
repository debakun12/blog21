# Generated by Django 3.2.4 on 2021-06-22 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0006_alter_feed_display_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedtable',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedtable', to=settings.AUTH_USER_MODEL),
        ),
    ]
