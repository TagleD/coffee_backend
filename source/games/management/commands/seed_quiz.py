from django.core.management.base import BaseCommand
from games.models import QuizQuestion


class Command(BaseCommand):
    help = "Заполняет базу примерными квиз-вопросами"

    def handle(self, *args, **kwargs):
        sample_questions = [
            {
                "question": "Какой напиток содержит больше всего кофеина?",
                "option_a": "Чай",
                "option_b": "Кофе",
                "option_c": "Какао",
                "option_d": "Матча",
                "correct_option": "B",
            },
            {
                "question": "Сколько грамм в одной столовой ложке кофе?",
                "option_a": "5 г",
                "option_b": "7 г",
                "option_c": "10 г",
                "option_d": "15 г",
                "correct_option": "C",
            },
            {
                "question": "Что означает термин 'эспрессо'?",
                "option_a": "Медленный",
                "option_b": "Сжатый",
                "option_c": "Быстрый",
                "option_d": "Темный",
                "correct_option": "C",
            },
            {
                "question": "Какая страна является родиной кофе?",
                "option_a": "Бразилия",
                "option_b": "Колумбия",
                "option_c": "Эфиопия",
                "option_d": "Вьетнам",
                "correct_option": "C",
            },
            {
                "question": "Какой помол кофе используется для турки (джезвы)?",
                "option_a": "Крупный",
                "option_b": "Средний",
                "option_c": "Тонкий",
                "option_d": "Очень тонкий",
                "correct_option": "D",
            },
        ]

        for q in sample_questions:
            QuizQuestion.objects.update_or_create(
                question=q["question"],
                defaults={
                    "option_a": q["option_a"],
                    "option_b": q["option_b"],
                    "option_c": q["option_c"],
                    "option_d": q["option_d"],
                    "correct_option": q["correct_option"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Вопросы успешно добавлены!"))
