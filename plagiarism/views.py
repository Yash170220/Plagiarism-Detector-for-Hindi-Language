from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from plagiarism.algorithm import similarity



def home(request):
    return render(request, 'index.html') 

@api_view(['POST'])
def checker(request):
    data=request.data
    query=data['text']
    
    result=similarity.similarity(query)
    percent=result['similarity']
    content=result['content']
    return render(request, 'index.html',{'text':query,'content':content,'percent': percent})