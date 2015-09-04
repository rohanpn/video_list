from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import View
from .models import User
from videos.views import  VideoListView
from .forms import VideoUserForm
from videos.decorators import post_method

# Create your views here.



class VideoLoginView(View):

    form = VideoUserForm

    def set_session_cookie(self, *args, **kwargs):
        request = self.request
        user_name = kwargs['user_name']
        request.session['user_name']=user_name
        response = redirect(reverse('list_video'))
        response.set_cookie('user_name', user_name)
        return response

    def post(self, *args, **kwargs):
        request = self.request
        form = VideoUserForm(self.request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['name']
            if User.objects.filter(user_name=user_name).exists():
                password = form.cleaned_data['password']
                user = User.objects.get(user_name=user_name)
                if user.password != password:
                    return render(request, 'User/login.html', {'error': 'Incorrect Password'})
            else:
                return render(request, 'User/login.html', {'error': 'No such user registered'})
            return self.set_session_cookie(self, user_name=user_name)
        else:
            return render(request, 'User/login.html', {'error': 'Invalid login details'})


class VideoLogoutView(View):

    def get(self, *args, **kwargs):
        request = self.request
        del request.session['user_name']
        response = render(request, 'home.html')
        response.delete_cookie('user_name')
        return response


class VideoRegisterView(View):

    def post(self, *args, **kwargs):
        request = self.request
        user_name = request.POST['user_name']
        email_id = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(user_name=user_name).exists() or User.objects.filter(email_id=email_id).exists():
            return render(request, 'User/register.html', {'error' :"Username or Email-id already exist,"
                                                                     " Please register with different user name."})
        if password != confirm_password:
            return render(request, 'User/register.html', {'error' :"Password didn't match."})
        User.objects.create(user_name= user_name, email_id=email_id,
                            password=password, date_joined=timezone.now())
        return render(request, 'User/login.html')


def video_register_view(request):
    """
        Register User to the app.
    """
    user_name = request.POST['user_name']
    email_id = request.POST['email_id']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if User.objects.filter(user_name=user_name).exists() or User.objects.filter(email_id=email_id).exists():
        return render(request, 'User/register.html', {'error' :"Username or Email-id already exist,"
                                                                 " Please register with different user name."})
    if password != confirm_password:
        return render(request, 'User/register.html', {'error' :"Password didn't match."})
    User.objects.create(user_name= user_name, email_id=email_id,
                        password=password, date_joined=timezone.now())
    return render(request, 'User/login.html')

