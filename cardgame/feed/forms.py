from feed.models import feed, feedtable
from crispy_forms.helper import FormHelper

from django import forms

from django.forms import ModelForm, fields

from feed.models import feed


class UploadFileForm(forms.ModelForm):
    # feedtable = forms.ModelChoiceField(
    #   queryset=feedtable.objects.filter(nameoftable="normal_feed"))

    class Meta:
        model = feed
        fields = ['display_title', 'display_text',
                  'content_blog', 'display_photo']
        exclude = ("nameoftable",)

    display_title = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={'style': 'text-align:center;font-size:40px ;width:100%;font-family: "Times New Roman", Times, serif; ', 'placeholder': 'Enter Blog Title', 'class': 'textboxa'}))
    content_blog = forms.CharField(widget=forms.Textarea(
        attrs={'style': 'text-align:center;font-size:40px ;width:100%;font-family: "Times New Roman", Times, serif;', 'placeholder': 'Enter Blog Content'}))
    display_text = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={'style': 'text-align:center;font-size:25px ;width:100%;font-family: "Times New Roman", Times, serif;'}))
