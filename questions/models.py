from django.db import models


class Level(models.Model):
    levels = models.IntegerField(unique= True)
    reading_range_high = models.IntegerField(unique=True)
    reading_range_low = models.IntegerField(unique=True)


class LevelWords(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,)
    word = models.TextField(unique=True)  # only noun, verb, adjective, adverb


class LevelQuestion(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,)
    question_text = models.TextField(unique=True)  # only noun, verb, adjective, adverb
    choice1 = models.TextField(unique=True)
    choice2 = models.TextField(unique=True)
    choice3 = models.TextField(unique=True)
    choice4 = models.TextField(unique=True)
    correct = models.IntegerField() #1,2,3,4
    feedback = models.TextField(blank=True,unique=True)
    date = models.DateField()
    #modified_date = models.DateField(blank=True)