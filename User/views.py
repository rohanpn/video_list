from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import TemplateView

from .models import User

from videos.views import list_videos
# Create your views here.
def login(request):
    """
        Login User
    """

    user_name = request.POST['name']
    if  User.objects.filter(user_name=user_name).exists():
        password = request.POST['password']
        user = User.objects.get(user_name=user_name)
        if user.password != password:
           return render(request, 'User/login.html', {'error': 'Incorrect password'})
    else:
        return render(request, 'User/login.html', {'error': 'No such user registered'})


    response = redirect(list_videos)
    response.set_cookie('user_name', user_name)
    return response


def logout(request):
    response = render(request, 'home.html')
    response.delete_cookie('user_name')
    return response

def register(request):
    """
        Register User
    """
    # import ipdb; ipdb.set_trace()

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

