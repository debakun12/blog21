from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# add author name, date,  to models


class feedtable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="feedtable", null=True)  # <--- added
    descrip = models.CharField(max_length=200)
    nameoftable = models.CharField(max_length=200)

    def __str__(self):
        return self.nameoftable


class feed(models.Model):
    feed_table = models.ForeignKey(feedtable, on_delete=models.CASCADE)
    display_title = models.CharField(max_length=200, null=True)
    display_text = models.CharField(max_length=200, null=True)
    content_blog = models.CharField(max_length=1000, null=True)
    display_link = models.CharField(max_length=200, null=True)
    uploadto = 'images'
    display_photo = models.ImageField(
        upload_to=uploadto, null=True)

    def __str__(self):
        return self.display_title
