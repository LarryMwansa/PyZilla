# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#    return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myPage.html')
  return HttpResponse(template.render())