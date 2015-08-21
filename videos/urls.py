from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.list_videos, name='list_video'),
    url(r'^add/', views.add_video, name='add_video'),
    url(r'^upload/', views.upload_video, name='upload_video'),
    url(r'^(?P<video_id>[0-9]+)/delete/', views.delete_video, name='delete_video'),
    url(r'^(?P<video_id>[0-9]+)/$', views.details, name='details'),
]