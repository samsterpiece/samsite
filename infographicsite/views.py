import json
import logging

import requests
from django.core.serializers import serialize

import os
from django.views.static import serve
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from infographicsite import infoparse
from .models import FilesUpload


# Create your views here.
#Passing information into the template
#still return an http response



def home2(request):
    #This method serves the purpose of receiving the data
    #uploaded to the server.
    if requests.get == "GET":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file = file2) #file2 saves the JSON object
        return HttpResponse("Your file was saved")


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
        return render(request, "index.html", { "context": context })
    elif request.method == "GET":
        return render(request, "index.html", {})
    else:
        return HttpResponse("Oops")

#exposing a POST endpoint without security authentication
@csrf_exempt
def analyze_data(request):
    if request.method == "POST":
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # expectedType = body['contentType']
        # expectedType = request.POST.get('contentType')
        jsonData = json.loads(request.FILES["file"].read())
        results = infoparse.processData(jsonData)
        # if request.META["HTTP_ACCEPT"] == "application/json":
        print("accept json")
        processedUserData = infoparse.processData(jsonData)
        response = JsonResponse(processedUserData)
        # response['Content-Type'] = expectedType
        response['Content-Disposition'] = 'attachment; filename=export.json'
        return response
        # elif request.META["HTTP_ACCEPT"] == "application/xml":
        #     print("accept xml")


        # #return xml.somefunc(xmlResponse(jsonData))
        # elif request.META["HTTP_ACCEPT"] == "text/plain":
        #     # return plainTextResponse(jsonData)
        #     return HttpResponse("Hello")
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