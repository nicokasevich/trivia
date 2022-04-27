from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from app.trivia.models import Category, Question, Answer


def home(request):
    return render(request, "trivia/home.html")


class SelectCategory(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, "trivia/category.html", {"categories": categories})

    def post(self, request, *args, **kwargs):
        category_id = request.POST.get("category", None)
        category = Category.objects.get(pk=category_id)
        if category:
            return redirect("trivia:play", category_id=category_id)
        return redirect("category")


class Play(View):
    def get(self, request, category_id, *args, **kwargs):
        category = Category.objects.get(pk=category_id)
        if not category:
            return redirect("trivia:category")

        known = request.session.get("known", [])
        question = (
            Question.objects.filter(category=category_id)
            .exclude(id__in=known)
            .order_by("?")
            .first()
        )
        if not question:
            return render(
                request,
                "trivia/category-completed.html",
                context={"category": category},
            )

        return render(request, "trivia/play.html", context={"question": question})


class ShowAnswer(View):
    def get(self, request, answer_id, *args, **kwargs):
        known = request.session.get("known", [])
        answer = get_object_or_404(Answer, pk=answer_id)
        if answer.is_correct:
            known.append(answer.question.id)
            request.session["known"] = known
        return render(request, "trivia/show-answer.html", context={"answer": answer})


def reset_questions(request):
    del request.session["known"]
    return redirect("trivia:category")
