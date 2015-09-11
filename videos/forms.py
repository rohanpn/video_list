from django.forms.models import ModelForm

__author__ = 'rohan'


from django import forms


class VideoForm(forms.Form):

    name = forms.CharField(max_length=200)
    size = forms.IntegerField()
    published =forms.DateField()
    file = forms.FileField()

    def clean(self):
        import ipdb;ipdb.set_trace()


class UserForm(ModelForm):
    name = forms.CharField()
