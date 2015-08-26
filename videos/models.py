from django.db import models
from User.models import User
#Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField(help_text='size in bytes')
    published = models.DateField(auto_now_add=True)
    file = models.FileField()
    user_key = models.ForeignKey(User)

    def __str__(self):
        return self.name

