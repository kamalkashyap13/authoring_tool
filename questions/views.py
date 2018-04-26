from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Level, LevelWords, LevelQuestion
from django.db.models import Q

#import en_core_web_sm
from textstat.textstat import textstat


def index(request):
    template = loader.get_template('questions/index.html')
    level_detail = Level.objects.all()
    vocab_detail = LevelWords.objects.all()
    ques_detail = LevelQuestion.objects.all()
    #  {"a":{"b":"EE"} }
    level_dict = {}
    vocab_dict = {}
    ques_dict = {}
    for i in range(len(level_detail)):
        level_no = level_detail[i].levels
        level_low = level_detail[i].reading_range_low
        level_high = level_detail[i].reading_range_high
        level_name = "Level " + str(level_no)
        level_range = str(level_high) + " - " + str(level_low)
        level_dict[level_name] = {"range": level_range}
        vocab_dict[level_name] = []
        ques_dict[level_name] = 0

    for i in range(len(vocab_detail)):
        level_no = vocab_detail[i].level.levels
        word = vocab_detail[i].word
        level_name = "Level " + str(level_no)
        vocab_dict[level_name].append(word)

    for i in range(len(ques_detail)):
        level_no = vocab_detail[i].level.levels
        level_name = "Level " + str(level_no)
        ques_dict[level_name]+=1

    context = {
        'level_range_detail': level_dict,
        'level_vocab_detail': vocab_dict,
        'level_ques_detail': ques_dict
    }
    return HttpResponse(template.render(context, request))


def sample(request):
    template = loader.get_template('questions/index.html')
    context = {
        "a": 1
    }
    return HttpResponse(template.render(context, request))


def question_add(request):
    if request.method == 'POST':
        question_txt = request.POST.get('question_txt')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        option_choice = request.POST.get('option_choice')
        level_no = int(request.POST.get('level_no'))

        level_detail = Level.objects.filter(Q(levels=level_no))[0]
        vocab_detail = LevelWords.objects.filter(Q(level=level_detail))
        all_vocab =[]
        level_low = level_detail.reading_range_low
        level_high = level_detail.reading_range_high
        for i in range(len(vocab_detail)):
            all_vocab.append(vocab_detail[i].word)

        score = textstat.flesch_reading_ease(question_txt)
        #nlp = en_core_web_sm.load()
        #doc = nlp(question_txt)

        for token in doc:
            if token.pos_ in ["VERB","NOUN","ADJ","ADV"]:
                lem = token.lemma_.lower()
                if lem in all_vocab:
                    good=1
                else:
                    return JsonResponse({"score": 1,"word":lem}, safe=False)
        return JsonResponse({"score": 1}, safe=False)



# front end
# verify, show error  - dependency - django 2.4, pip install textstat, spacy
# pip install -U spacy, python -m spacy download en
# show question for edit
# add data
# git
# live
# domain

#cumulative vocab