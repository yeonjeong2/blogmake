from django import forms
from .models import comment

class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']