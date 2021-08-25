from .models import Video
from django import forms
#there are model based forms and then there are regular forms that we can create.

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'YouTube Url'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label = "search for videos")

    #the user shouldn't be able to select the hall. Instead they should be using the hall that
    #they're aldready looking at. 

