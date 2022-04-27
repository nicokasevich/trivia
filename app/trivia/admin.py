from django.contrib import admin
from app.trivia.models import Category, Question, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 5


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question"]
    inlines = [AnswerInline]
