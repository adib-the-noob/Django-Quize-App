from django.contrib import admin
from .models import Category, Question, Answer
# Register your models here.
admin.site.register(Category)


class AnsweAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnsweAdmin]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
