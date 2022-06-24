from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Tradução de arquivos.")


@csrf_exempt
def upload(request):
    teste = request.FILES
    data = dateProcessing(request.FILES)
    return data



def dateProcessing(file):
    return 'teste leitura'