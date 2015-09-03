from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.vary import vary_on_headers
from django.views.generic.base import TemplateView
from videos.views import AddVideoView

urlpatterns = [
    url(r'^add/', AddVideoView.as_view(), name='add_video'),
    url(r'^upload/', views.VideoUploadView.as_view(), name='upload_video'),
    url(r'^(?P<pk>[0-9]+)/delete/', views.VideoDeleteView.as_view(), name='delete_video'),
    url(r'^(?P<pk>[0-9]+)/$', views.VideoDetailView.as_view(), name='details'),
    url(r'^$', views.VideoListView.as_view(), name='list_video'),
]
