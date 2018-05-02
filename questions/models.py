from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    levels = models.IntegerField(unique= True)
    reading_range_high = models.IntegerField(unique=True)
    reading_range_low = models.IntegerField(unique=True)

    def __str__(self):
        return "Level " +  str(self.levels)


class LevelWords(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,)
    word = models.TextField(unique=True)  # only noun, verb, adjective, adverb


class LevelQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comprehension = 1
    vocabulary = 2
    grammar = 3
    type_field = (('', '---------'), (comprehension, 'comprehension'), (vocabulary, 'vocabulary'),
                   (grammar, 'grammar'))
    politics = 1
    sports = 2
    science = 3
    entertainment = 4
    world = 5
    nation = 6
    environment = 7
    business_and_commerce = 8
    tech = 9
    lifestyle = 10
    others = 11
    genre_field = (('', '---------'), (politics, 'politics'), (tech, 'tech'),
                   (lifestyle, 'lifestyle'),
                   (sports, 'sports'),
                   (science, 'science'), (entertainment, 'entertainment'), (world, 'world'), (nation, 'nation'),
                   (environment, 'environment'), (business_and_commerce, 'business and commerce'), (others, 'others'))
    level = models.ForeignKey(Level, on_delete=models.CASCADE, )
    question_category = models.IntegerField(choices=type_field)
    question_genre = models.IntegerField(choices=genre_field)
    question_inst = models.TextField()
    question_text = models.TextField(unique=True)  # only noun, verb, adjective, adverb
    choice1 = models.TextField()
    choice2 = models.TextField()
    choice3 = models.TextField()
    choice4 = models.TextField()
    correct = models.IntegerField() #1,2,3,4
    feedback = models.TextField(blank=True)
    #date = models.DateField()
    contact_time = models.TimeField( auto_now_add=True, blank=True, null=True,)
    #modified_date = models.DateField(blank=True)