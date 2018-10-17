from django.shortcuts import render
from .models import ChatBotQuestion
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse
import json 


def index(request):
    """
    This function to take on first page of chatbot
    """
    return render(request,'chatbot/chat.html')

@csrf_exempt
def search(request):
    """ This function is to get result from data base based on query passed from function"""
    
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        input_value = json_data.get('input')
        text_name   =    input_value.replace('"', '').replace("'", '')
        text_name  = text_name.strip()
        queryset =   ChatBotQuestion.objects.get(question_text=text_name)
        if queryset is not None:
            output_message = queryset.answer_text
            response_message = {'message':output_message}
            return JsonResponse(response_message)    


    
