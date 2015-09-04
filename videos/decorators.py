from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from User.models import User


def required_login(func=None):
    """
        Decorator to check whether the user is logged in .
    """
    def cookie_wrap(self, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        if self.request.COOKIES.has_key('user_name') and self.request.session.has_key('user_name'):
            user = self.request.COOKIES.get('user_name')
            if User.objects.filter(user_name=user).exists():
                if user == self.request.session.get('user_name'):
                    return func(self, *args, **kwargs)
        return render(self.request, 'home.html', {'error': 'You must be Logged In to Continue.'})

    return cookie_wrap




def req_login(func=None):
    def cookie_wrap(request, *args, **kwargs):
        import ipdb;ipdb.set_trace()

        if request.COOKIES.has_key('user_name') and request.session.has_key('user_name'):
            user = request.COOKIES.get('user_name')
            if User.objects.filter(user_name=user).exists():
                if user == request.session.get('user_name'):
                    return func(request, *args, **kwargs)
        return render(request, 'home.html', {'error': 'You must be Logged In to Continue.'})
    return cookie_wrap


def post_method(func=None):
    """
        Decorator to check whether the method is post method

    """
    def check_method(request, *args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return render(request, 'home.html', {'error':"You can use only post method."})
    return check_method


def get_method(func=None):
    """
        Decorator to check whether the method is get method
    """
    def check_method(request, *args, **kwargs):
        if request.method == 'GET':
            return func(request, *args, **kwargs)
        else:
            return render(request, 'home.html', {'error':"You can use only get method."})
    return check_method
