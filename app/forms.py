from django import forms
from .models import Directory, Record


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'parent', 'image']


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content', 'directory', 'description']