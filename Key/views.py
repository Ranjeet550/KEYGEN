from django.shortcuts import render


def home(request):

    return render(request, 'Key/home.html', {'title':'Home'})
