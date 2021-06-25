from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import feed, feedtable
from .forms import UploadFileForm
from math import ceil
from django.contrib.auth.models import User
# Create your views here.


def feed(response, u_name):
    #    if response.method == "POST":
    #       id_new = id+1
    #        return HttpResponseRedirect("/feed/"+str(id_new))
    uid = User.objects.get(username=u_name)
    feed_table = uid.feedtable.all()[0]
    descrip = feed_table.descrip
    feed_set = feed_table.feed_set.all()
    last_page = ceil(feed_set.count()/2)
    return render(response, "feed/feed_page.html", {'feed_set': feed_set, 'u_name': u_name, 'descrip': descrip})


def blog_open(response, u_name,  b_name):
    uid = User.objects.get(username=u_name)
    feed_table = uid.feedtable.all()[0]
    descrip = feed_table.descrip
    feed_set = feed_table.feed_set.all()
    blog = feed_set.filter(display_link=b_name)[0]
    id = int(ceil(blog.id/2))
    return render(response, "feed/blog_page.html", {"descrip": descrip, "blog": blog, "id_prev": id, "u_name": u_name})


def blog_create(response):
    if response.method == "POST":
        form = UploadFileForm(data=response.POST, files=response.FILES)
        if form.is_valid():
            uid = User.objects.get(username=response.user.username)
            try:
                display_link = uid.feedtable.filter(
                    nameoftable=response.user.username)[0].feed_set.all()
            except:
                tablee = feedtable(nameoftable=response.user.username)
                tablee.user = uid
                tablee.save()

                display_link = response.user.feedtable.filter(
                    nameoftable=response.user.username).feed_set.all()

            display_link = display_link.count()
            display_link = response.user.username + str(display_link)

            feedd = form.save(commit=False)
            feedd.display_link = display_link
            feedd.feed_table = uid.feedtable.all()[0]

            feedd.save()

    else:
        form = UploadFileForm()
    return render(response, "feed/new_blog.html", {"form": form})
