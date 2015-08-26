from django.http import HttpResponse
from django.shortcuts import render


def cookie_required(func=None):
    """
        Decorator to check whether the user is logged in .
    """
    def cookie_wrap(request, *args, **kwargs):
        val = request.COOKIES.has_key('user_name')
        if val:
            return func(request, *args, **kwargs)
        else:
            return render(request, 'home.html', {'error': 'You must be Logged In to Continue.'})
    return cookie_wrap

