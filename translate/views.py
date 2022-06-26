from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from translate.tools.dataProcessing import handle_file_upload
from django.core.serializers import serialize
import json


def index(request):
    return HttpResponse("Tradução de arquivos.")


@csrf_exempt
def upload(request):
    returnData = handle_file_upload(request.FILES['file'])
    #data = serialize("json", returnData, fields=('title', 'content'))
    teste = json.dumps(returnData)
    return HttpResponse(teste, content_type="application/json")