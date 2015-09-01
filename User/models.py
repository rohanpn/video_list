from django.db import models
# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    password = models.CharField(max_length=200)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

