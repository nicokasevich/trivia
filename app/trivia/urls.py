from django.urls import path
import app.trivia.views as views

app_name = "Trivia"

urlpatterns = [
    path("", views.home, name="home"),
    path("category", views.SelectCategory.as_view(), name="category"),
    path("<category_id>/play", views.Play.as_view(), name="play"),
    path(
        "answer/<answer_id>",
        views.ShowAnswer.as_view(),
        name="answer",
    ),
    path("reset-questions", views.reset_questions, name="reset-questions"),
]
