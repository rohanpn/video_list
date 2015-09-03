from django.core.urlresolvers import reverse
from django.http.response import HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView
from .models import Video, User
from .decorators import required_login, req_login


class VideoListView(ListView):

    template_name = "videos/index.html"
    context_object_name= 'video_list'

    @required_login
    def get_queryset(self, *args, **kwargs):
        user_name = self.request.COOKIES['user_name']
        video_details  = Video.objects.filter(user_key= User.objects.get(user_name=user_name).id)
        return video_details


class AddVideoView(View):
    """
        View to render the  template to add the video.
    """
    template_name = "videos/add_video.html"


    def post(self, *args, **kwargs):
        """
            Need of the method is because the request made is post
        """
        return render(self.request, self.template_name)


class VideoUploadView(CreateView):
    """
        Upload a Video in the database
    """

    def get_queryset(self, *args, **kwargs):
        context = super(VideoUploadView, self).get_queryset(self)
        return context

    def post(self, request, *args, **kwargs):
        user_obj = User.objects.get(user_name=self.request.COOKIES.get('user_name'))
        file_details= self.request.FILES['file_name']
        if file_details.content_type.startswith('video/'):
            Video.objects.create(user_key=user_obj, name=file_details.name, size=file_details.size,
                                 published = timezone.now(), file=file_details)
            return redirect(reverse('list_video'))
        else:
            return HttpResponseBadRequest("Invalid video Format.")


class VideoDetailView(DetailView):
    template_name = "videos/detail.html"
    context_object_name = "video"
    model = Video


class VideoDeleteView(DeleteView):
    template_name = "videos/video_deleted.html"
    context_object_name = 'video_list'
    model = Video

    def get_context_data(self, **kwargs):
        context = super(VideoDeleteView, self).get_context_data()
        video_details=Video.objects.get(pk=self.kwargs['pk'])
        video_details.file.delete()
        video_details.delete()
        context['video_list'] = video_details
        return context

