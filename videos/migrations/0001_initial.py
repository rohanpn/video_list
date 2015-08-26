# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('size', models.IntegerField(help_text=b'size in bytes')),
                ('published', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'')),
                ('user_key', models.ForeignKey(to='User.User')),
            ],
        ),
    ]
