
import User
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from User.views import VideoLoginView, VideoLogoutView, VideoRegisterView

urlpatterns = [

    url(r'^login/validate/', VideoLoginView.as_view(), name='login_validate'),
    url(r'^login/', TemplateView.as_view(template_name='User/login.html'), name='login'),
    url(r'^register/', TemplateView.as_view(template_name='User/register.html'), name='register'),
    url(r'^register_user/', VideoRegisterView.as_view(), name='register_user'),
    url(r'logout/', VideoLogoutView.as_view(), name='logout')
]