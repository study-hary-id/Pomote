from django.db import models


class Question(models.Model):
    question_text = models.TextField()


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
