from datetime import datetime

from django.test import TestCase
from django.utils import timezone
fron django.urls import reverse

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_published_recently_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_old(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.published_recently(), False)

    def test_published_recently_recent(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)



def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


