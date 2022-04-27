from django.core.management.base import BaseCommand
from django_seed import Seed
from app.trivia.models import Question, Answer, Category


class Command(BaseCommand):
    help = "Adds questions with its answers and categories."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(Category, 1, {"name": "Sports"})
        seeder.add_entity(Category, 1, {"name": "History"})
        seeder.add_entity(Category, 1, {"name": "Music"})

        seeder.execute()

        sports = Category.objects.get(pk=1)
        history = Category.objects.get(pk=2)
        music = Category.objects.get(pk=3)

        seeder.add_entity(
            Question,
            1,
            {
                "question": "What’s the diameter of a basketball hoop in inches?",
                "category": sports,
            },
        )

        seeder.execute()
        question_1 = Question.objects.get(pk=1)

        seeder.add_entity(
            Answer,
            1,
            {"answer": "18 inches", "is_correct": True, "question": question_1},
        )
        seeder.add_entity(Answer, 1, {"answer": "14 inches", "question": question_1})
        seeder.add_entity(Answer, 1, {"answer": "20 inches", "question": question_1})
        seeder.add_entity(Answer, 1, {"answer": "22 inches", "question": question_1})
        seeder.add_entity(Answer, 1, {"answer": "15 inches", "question": question_1})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "The Olympics are held every how many years?",
                "category": sports,
            },
        )

        seeder.execute()
        question_2 = Question.objects.get(pk=2)

        seeder.add_entity(Answer, 1, {"answer": "3 years", "question": question_2})
        seeder.add_entity(
            Answer, 1, {"answer": "4 years", "is_correct": True, "question": question_2}
        )
        seeder.add_entity(Answer, 1, {"answer": "5 years", "question": question_2})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "What sport is best known as the ‘king of sports’?",
                "category": sports,
            },
        )

        seeder.execute()
        question_3 = Question.objects.get(pk=3)

        seeder.add_entity(
            Answer, 1, {"answer": "Soccer", "is_correct": True, "question": question_3}
        )
        seeder.add_entity(Answer, 1, {"answer": "Basketball", "question": question_3})
        seeder.add_entity(Answer, 1, {"answer": "Football", "question": question_3})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "Greenland was a colony of which country until 1981?",
                "category": history,
            },
        )

        seeder.execute()
        question_4 = Question.objects.get(pk=4)

        seeder.add_entity(Answer, 1, {"answer": "UK", "question": question_4})
        seeder.add_entity(
            Answer, 1, {"answer": "Denmark", "is_correct": True, "question": question_4}
        )
        seeder.add_entity(
            Answer, 1, {"answer": "United States", "question": question_4}
        )

        seeder.add_entity(
            Question,
            1,
            {
                "question": "How many days in a week were there in ancient Roman times?",
                "category": history,
            },
        )

        seeder.execute()
        question_5 = Question.objects.get(pk=5)

        seeder.add_entity(Answer, 1, {"answer": "6", "question": question_5})
        seeder.add_entity(
            Answer, 1, {"answer": "8", "is_correct": True, "question": question_5}
        )
        seeder.add_entity(Answer, 1, {"answer": "7", "question": question_5})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "In which year was John F. Kennedy assassinated?",
                "category": history,
            },
        )

        seeder.execute()
        question_6 = Question.objects.get(pk=6)

        seeder.add_entity(Answer, 1, {"answer": "1960", "question": question_6})
        seeder.add_entity(Answer, 1, {"answer": "1962", "question": question_6})
        seeder.add_entity(
            Answer, 1, {"answer": "1963", "is_correct": True, "question": question_6}
        )

        seeder.add_entity(
            Question,
            1,
            {
                "question": "Van Halen famously banned what color M&Ms in their rider?",
                "category": music,
            },
        )

        seeder.execute()
        question_7 = Question.objects.get(pk=7)

        seeder.add_entity(Answer, 1, {"answer": "Purple", "question": question_7})
        seeder.add_entity(
            Answer, 1, {"answer": "Brown", "is_correct": True, "question": question_7}
        )
        seeder.add_entity(Answer, 1, {"answer": "Scarlet", "question": question_7})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "Prince introduced his iconic symbol on the cover of which single?",
                "category": music,
            },
        )

        seeder.execute()
        question_8 = Question.objects.get(pk=8)

        seeder.add_entity(
            Answer, 1, {"answer": "1999", "is_correct": True, "question": question_8}
        )
        seeder.add_entity(Answer, 1, {"answer": "1998", "question": question_8})
        seeder.add_entity(Answer, 1, {"answer": "2000", "question": question_8})

        seeder.add_entity(
            Question,
            1,
            {
                "question": "How many coaches (full and part-time) from The Voice have won Grammys?",
                "category": music,
            },
        )

        seeder.execute()
        question_9 = Question.objects.get(pk=9)

        seeder.add_entity(Answer, 1, {"answer": "8", "question": question_9})
        seeder.add_entity(
            Answer, 1, {"answer": "12", "is_correct": True, "question": question_9}
        )
        seeder.add_entity(Answer, 1, {"answer": "16", "question": question_9})

        seeder.execute()
