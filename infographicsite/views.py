from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import FilesUpload
import requests
from django.views.decorators.csrf import csrf_exempt

from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
import json
from infographicsite import infoparse
import logging

# Create your views here.
#Passing information into the template
#still return an http response



def home2(request):
    #This method serves the purpose of receiving the data
    #uploaded to the server.
    if requests.get == "GET":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file = file2) #file2 saves the JSON object
        return HttpResponse("Your file was savgeted")


# This method serves the purpose of posting the data to the admin side
# And saving it in file2.
def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        logger = logging.getLogger(__name__)
        # logger.error(file2.read())
        json_data = json.loads(file2.read())
        document = FilesUpload.objects.create(file = file2)
        context = infoparse.processData(json_data)
#     if request.method=='POST':
#         received_json_data=json.loads(request.POST['data'])
#         #received_json_data=json.loads(request.body)
#         return StreamingHttpResponse('it was post request: '+str(received_json_data))
#     return StreamingHttpResponse('it was GET request')
        return render(request, "results.html", { "context": context })
    elif request.method == "GET":
        return render(request, "index.html", {})
    else:
        return HttpResponse("Oops")

@csrf_exempt 
def analyze_data(request):
    if request.method == "POST":
            return HttpResponse("Hello")
    else:
       raise Http404("Error")

# def home(request):
#     if request.method == "POST":
#         data = json.load(request.FILES["file"].read())
#         userCount = len(data['results'])
#         firstFirstName = data['results'][0]['name']['first']
#         context = { "count":userCount, "ffName":firstFirstName }
#         return render(request, "index.html", context)
#     return render(request, "index.html")

