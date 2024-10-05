from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def about(request):
    myabout = Member.objects.all().values()
    template = loader.get_template('about.html')
    context = {
        'myabout': myabout,
  } 
    return HttpResponse(template.render(context, request))
