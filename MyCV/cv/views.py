from django.shortcuts import render
from .models import Profile


def homepage(request):
    profiles = Profile.objects.all()
    return render(request, 'homepage.html', context={"profiles": profiles})
