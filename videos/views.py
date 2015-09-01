from django.http.response import HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Video, User
from .decorators import required_login



@required_login
def list_videos_view(request):
    """
        List all titles of the videos available for the logged-in user.
    """
    video_list = Video.objects.filter(user_key=User.objects.get(user_name=request.COOKIES['user_name']).id)
    context = {'video_list': video_list }
    return render(request, 'videos/index.html', context)


@required_login
def add_video_view(request):
    """
        Add a video for the current logged-in user.
    """
    return render(request, 'videos/add_video.html')


@required_login
def upload_video_view(request):
    """
        Upload video in the database
    """
    user_obj = User.objects.get(user_name=request.COOKIES.get('user_name'))
    file_details = request.FILES['file_name']

    if file_details.content_type.startswith('video/'):
        Video.objects.create(user_key=user_obj, name=file_details.name, size=file_details.size,
                             published = timezone.now(), file=file_details)
        return redirect(list_videos_view)
    else:
        return HttpResponseBadRequest("Invalid video Format.")


@required_login
def details_view(request, video_id):
    """
        List all the details of the video
    """
    if Video.objects.filter(id=video_id).exists():
        video_details=Video.objects.get(id= video_id)
        context = {'video': video_details}
    else:
        raise Http404

    return render(request, 'videos/detail.html', context)


@required_login
def delete_video_view(request, video_id):
    """
        Delete the selected record from the database for the current logged in user.
    """
    video_details=Video.objects.get(pk=video_id)
    video_details.file.delete()
    video_details.delete()
    return redirect(list_videos_view)



