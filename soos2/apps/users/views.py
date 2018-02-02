from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

    elif request.method == 'GET':
        return render(request, 'login.html', {})
