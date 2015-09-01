from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from videos.views import list_videos_view
from .forms import VideoUserForm
from videos.decorators import post_method

# Create your views here.


def video_login_view(request):
    """
        Login User
    """
    if request.method == "POST":

        form = VideoUserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            if User.objects.filter(user_name=user_name).exists():

                password = form.cleaned_data['password']
                user = User.objects.get(user_name=user_name)
                if user.password != password:
                   return render(request, 'User/login.html', {'error': 'Incorrect password'})
            else:
                return render(request, 'User/login.html', {'error': 'No such user registered'})
            request.session['user_name']=user_name
            response = redirect(list_videos_view)
            response.set_cookie('user_name', user_name)
            return response
        else:
            return render(request, 'User/login.html', {'error': 'Invalid login details'})


def video_logout_view(request):
    """
        Logout the current logged in user.
    """
    del request.session['user_name']
    request.session.modified = True
    response = render(request, 'home.html')
    response.delete_cookie('user_name')
    return response


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

