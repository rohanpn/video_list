from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.vary import vary_on_headers
from .models import Video, User
from .decorators import login_check
from .forms import VideoForm


@login_check
def list_videos_view(request):
    """
        List all titles of the videos available
    """

    video_list = Video.objects.filter(user_key=User.objects.get(user_name=request.COOKIES['user_name']).id)
    context = {'video_list' : video_list}
    return render(request, 'videos/index.html', context)


@login_check
def add_video_view(request):
    """
        Add a video
    """
    return render(request, 'videos/add_video.html')


@login_check
def upload_video_view(request):
    """
        Upload video in the database
    """
    user_obj = User.objects.get(user_name=request.COOKIES.get('user_name'))
    file_details = request.FILES['file_name']

    if file_details.content_type.startswith('video/'):
        Video.objects.create(user_key=user_obj, name=file_details.name, size=file_details.size,
                             published = timezone.now(),
                              file=file_details)

        return redirect(list_videos_view)
    else:
        return HttpResponseBadRequest("Invalid video Format.")


@login_check
def details_view(request, video_id):
    """
        List all the details of the video
    """
    id = User.objects.get(user_name=request.COOKIES.get('user_name')).id
    # vd = Video.objects.filter(user_key=User.objects.filter(id=id))
    video_details=Video.objects.get(id= video_id)
    context = {'video': video_details}
    return render(request, 'videos/detail.html', context)

@login_check
def delete_video_view(request, video_id):
    """
        Delete the record from the database
    """
    video_details=Video.objects.get(pk=video_id)
    video_details.file.delete()
    video_details.delete()
    return redirect(list_videos_view)



