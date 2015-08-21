from django.contrib import admin

from .models import Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    fields = ['video_published', 'video_name']



admin.site.register(Video, VideoAdmin)
