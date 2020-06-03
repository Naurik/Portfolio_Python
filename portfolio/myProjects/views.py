from django.shortcuts import render
from .models import MyProject


def project_list(request):
    project = MyProject.objects.all()
    return render(request,
                  'mainPage/main.html',
                  {'project': project})

