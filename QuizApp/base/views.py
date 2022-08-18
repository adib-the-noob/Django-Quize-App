from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Category, Question, Answer
import random
# Create your views here.

def get_quize(request):
    try:
        questions = list(Question.objects.all())
        data = []
        random.shuffle((questions))

        print()

        for question in questions:
            data.append({
                'category': question.category.category_name,
                'question': question.question,
                'marks': question.marks,
            })

        payload = {
            'status': 'success',
            'data': data
        }
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse('Something went wrong')
