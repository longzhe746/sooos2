from django.shortcuts import render
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None,**kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            user_login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg':'用户名密码错误!'})

    elif request.method == 'GET':
        return render(request, 'login.html', {})
