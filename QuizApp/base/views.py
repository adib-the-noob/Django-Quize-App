from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Category, Question, Answer
import random
# Create your views here.

def home(request):
    context = {
        'categories': Category.objects.all()
    }

    if request.GET.get("category"):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request, 'home.html',context)

def quiz(request):
    return render(request, 'quiz.html')


def get_quize(request):
    try:
        questions = (Question.objects.all())

        if request.GET.get("category"):
            questions = questions.filter(category__category_name__icontains=request.GET.get("category"))
        questions = list(questions)
        data = []
        random.shuffle((questions))

        # print(questions)

        for question in questions:
            # print(question.question)
            data.append({
                'category': question.category.category_name,
                'question': question.question,
                'marks': question.marks,
                'answers': question.get_answers(),
            })

        payload = {
            'status': 'success',
            'data': data
        }
        return JsonResponse(payload)
    except Exception as e:
        #print(e)
        return HttpResponse('Something went wrong')
