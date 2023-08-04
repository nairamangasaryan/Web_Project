from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    BLOG_TYPES = (
        ("1", "Sport"),
        ("2", "Travel"),
        ("3", "Handmade"),
        ("4", "Funny Animals"),
        ("5", "Nature")
    )

    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Title of Blog'}))
    description = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Your Blog Text'}))
    image = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Image For Your Blog'}))
    blog_type = forms.ChoiceField(choices=BLOG_TYPES)
    creation_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Blog
        fields = ["title", "description", "image",
                  "blog_type", "creation_date"]
