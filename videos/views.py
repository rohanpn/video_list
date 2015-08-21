from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Video, User
from django.contrib.auth.decorators import login_required


def list_videos(request):
    """
        List all titles of the videos available
    """
    if request.COOKIES.has_key('user_name'):
        video_list = Video.objects.all()
        context = {'video_list' : video_list}
        return render(request, 'videos/index.html', context)
    else:
        return render(request, 'home.html', {'error': 'Please login to continue'})

def add_video(request):
    """
        Add a video
    """
    if request.COOKIES.has_key('user_name'):
        return render(request, 'videos/add_video.html')
    return HttpResponseBadRequest("Page not Found")


def upload_video(request):
    """
        Upload video in the database
    """
    if request.COOKIES.has_key('user_name'):
        user_obj = User.objects.get(user_name=request.COOKIES.get('user_name'))
        file_details = request.FILES['file_name']

        if file_details.content_type.startswith('video/'):
            Video.objects.create(user_key=user_obj, name=file_details.name, size=file_details.size,
                                 published=timezone.now(), file=file_details)
            return redirect(list_videos)
        else:
            return HttpResponseBadRequest("Invalid video Format.")
    return HttpResponseBadRequest("Page not Found")


def details(request, video_id):
    """
        List all the details of the video
    """
    if request.COOKIES.has_key('user_name'):
        id = User.objects.get(user_name=request.COOKIES.get('user_name')).id
        # vd = Video.objects.filter(user_key=User.objects.filter(id=id))
        video_details=Video.objects.get(id= video_id)
        context = {'video': video_details}
        return render(request, 'videos/detail.html', context)
    return HttpResponseBadRequest("Page not Found")


def delete_video(request, video_id):
    """
        Delete the record from the database
    """
    if request.COOKIES.has_key('user_name'):
        video_details=Video.objects.get(pk=video_id)
        video_details.file.delete()
        video_details.delete()
        return redirect(list_videos)
    return HttpResponseBadRequest("Page not Found")



