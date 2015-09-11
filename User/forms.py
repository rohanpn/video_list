from django import forms
from django.core.exceptions import ValidationError
from videos.models import User
from django.forms import ModelForm

class VideoUserForm(forms.Form):

    name = forms.CharField(label="user_name", max_length=30, required=True)
    password = forms.CharField(label="password", max_length=200, required=True)

    def clean(self):
        """
        To check whether the user is registered or not.
        """

        cleaned_data = super(VideoUserForm, self).clean()
        user = cleaned_data['name']
        passwd = cleaned_data['password']
        if User.objects.filter(user_name=user).exists():
                user = User.objects.get(user_name=user)
                if user.password != passwd:
                    import ipdb;ipdb.set_trace()
                    raise forms.ValidationError("Invalid credentials.")
        else:
            raise forms.ValidationError("Invalid user.")



class VideoRegisterForm(forms.Form):

    user_name = forms.CharField(max_length=30)
    email_id = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()

    def clean(self):
        import ipdb;ipdb.set_trace()

        cleaned_data = super(VideoRegisterForm, self).clean()
        import ipdb;ipdb.set_trace()
        if 'email_id' in cleaned_data.keys():
            passwd = cleaned_data['password']
            confirm_password =cleaned_data['confirm_password']
            email_id=cleaned_data['email_id']
        raise forms.ValidationError("Invalid email field.")

