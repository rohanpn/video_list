
import User
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from User.views import login, logout, register
from User.models import User

urlpatterns = [

    url(r'^login/validate/', login, name='login_validate'),
    url(r'^login/', TemplateView.as_view(template_name='User/login.html'), name='login'),
    url(r'^register/', TemplateView.as_view(template_name='User/register.html'), name='register'),
    url(r'^register_user/', register, name='register_user'),
    url(r'logout/', logout, name='logout')
]