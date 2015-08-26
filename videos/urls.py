from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.vary import vary_on_headers

urlpatterns = [
    url(r'^$', views.list_videos_view, name='list_video'),
    url(r'^add/', views.add_video_view, name='add_video'),
    url(r'^upload/', views.upload_video_view, name='upload_video'),
    url(r'^(?P<video_id>[0-9]+)/delete/', views.delete_video_view, name='delete_video'),
    url(r'^(?P<video_id>[0-9]+)/$', views.details_view, name='details'),
]