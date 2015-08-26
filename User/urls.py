
import User
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from User.views import video_register_view, video_logout_view, video_login_view
from User.models import User

urlpatterns = [

    url(r'^login/validate/', video_login_view, name='login_validate'),
    url(r'^login/', TemplateView.as_view(template_name='User/login.html'), name='login'),
    url(r'^register/', TemplateView.as_view(template_name='User/register.html'), name='register'),
    url(r'^register_user/', video_register_view, name='register_user'),
    url(r'logout/', video_logout_view, name='logout')
]