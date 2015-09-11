from django.core.urlresolvers import reverse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView
from .models import Video, User
from .decorators import required_login
from videos.forms import VideoForm


class VideoListView(ListView):
    """
        list all the videos of the current logged in users.
        ListView: "object_list" in our case 'video_list' is executed.
            which we get with get_queryset(). hence, it is overridden
    """
    template_name = "videos/index.html"
    context_object_name= 'video_list'
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
        CreateView is used because it is used to save the object.
    """

    def get_queryset(self, *args, **kwargs):
        context = super(VideoUploadView, self).get_queryset(self)
        return context

    @required_login
    def post(self, request, *args, **kwargs):
        form = VideoForm(request.POST)
        user_obj = User.objects.get(user_name=self.request.COOKIES.get('user_name'))
        file_details= self.request.FILES['file_name']

        # Use form.is_multipart() instead
        if file_details.content_type.startswith('video/'):
            Video.objects.create(user_key=user_obj, name=file_details.name, size=file_details.size,
                                 published = timezone.now(), file=file_details)
            return redirect(reverse('list_video'))
        else:
            return HttpResponseBadRequest("Invalid video Format.")

class VideoDetailView(DetailView):
    """
        show the details of the current video selected
        DetailView: self.object contains the list of object provided to this view,
            here we have passed the pk of the model t
    """
    # template_name = "videos/video_detail.html"
    context_object_name = "video"
    model = Video


class VideoDeleteView(DeleteView):
    """
        Delete the video from the list of the videos
        DeleteView : To delete the existing object, the object is deleted
                only if the method is post.

    """
    template_name = "videos/video_deleted.html"
    context_object_name = 'video_list'
    model = Video

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDeleteView, self).get_context_data()
        video_details=Video.objects.get(pk=self.kwargs['pk'])
        video_details.file.delete()
        video_details.delete()
        context['video_list'] = video_details
        return context

