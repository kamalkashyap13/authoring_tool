from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    levels = models.IntegerField(unique= True)
    reading_range_high = models.IntegerField(unique=True)
    reading_range_low = models.IntegerField(unique=True)

    def __str__(self):
        return "Level " + str(self.levels)


class LevelWords(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,)
    word = models.CharField(max_length=25,unique=True)  # only noun, verb, adjective, adverb
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Word : " + str(self.word)


class OffWords(models.Model):
    level_word = models.ForeignKey(LevelWords, on_delete=models.CASCADE, )
    level_set = models.ForeignKey(Level, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=25)

    def __str__(self):
        return "User : " + str(self.user) + ", " + str(self.level_word)


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
    nature = 11
    leisure = 12
    travel = 13
    spiritual = 14
    fiction = 15
    others = 16
    genre_field = (('', '---------'), (politics, 'politics'),
                   (sports, 'sports'),
                   (science, 'science'), (entertainment, 'entertainment'), (world, 'world'), (nation, 'nation'),
                   (environment, 'environment'), (business_and_commerce, 'business and commerce'),
                   (tech, 'tech'),
                   (lifestyle, 'lifestyle'),
                   (nature, 'nature'), (leisure,'leisure'),
                   (travel,'travel'), (spiritual,'spiritual'),
                   (fiction,'fiction'),
                   (others, 'others'))
    level = models.ForeignKey(Level, on_delete=models.CASCADE, )

    question_category = models.IntegerField(choices=type_field)
    question_genre = models.IntegerField(choices=genre_field)
    que_format = models.CharField(max_length=20,blank=True)
    low = 1
    medium = 2
    high = 3
    diff_field = (('', '---------'), (low, 'low'), (medium, 'medium'),
                  (high, 'high'))
    difficulty = models.IntegerField(choices=diff_field)#1,2,3

    #
    concept = models.CharField(max_length=20,blank=True)
    sub_concept = models.CharField(max_length=20,blank=True)

    question_inst = models.CharField(max_length=200,blank=True)
    question_para = models.TextField(blank=True)#empty for grammar, only noun, verb, adjective, adverb
    question_text = models.CharField(max_length=200,unique=True)
    question_word = models.CharField(max_length=20, blank=True)
    #
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    correct = models.IntegerField()

    #
    option_create = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=200, blank=True)
    #
    feedback = models.CharField(max_length=20,blank=True)
    contact_time = models.TimeField( auto_now_add=True, blank=True, null=True,)

    def __str__(self):
        return "User : " + str(self.user) + ", " + "Level :" + str(self.level) \
               # + ", " + "Type : "\
               # + str(self.question_category)