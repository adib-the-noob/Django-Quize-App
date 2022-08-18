from re import A
from django.db import models
import uuid
import random

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='answers')
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer = list(Answer.objects.filter(question=self))
        random.shuffle(answer)
        data = []
        for ans in answer:
            data.append({
                'answer': ans.answer,
                'is_correct': ans.is_correct,
            })
        return data 


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='questions')
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer