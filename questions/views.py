from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Level, LevelWords, LevelQuestion
from django.db.models import Q
import nltk
from django.db import IntegrityError
#import en_core_web_sm
from textstat.textstat import textstat
import datetime
today = datetime.date.today()


def index(request):
    template = loader.get_template('questions/index.html')
    level_detail = Level.objects.all()
    vocab_detail = LevelWords.objects.all()
    ques_detail = LevelQuestion.objects.all().order_by('contact_time')
    #  {"a":{"b":"EE"} }
    level_dict = {}
    vocab_dict = {}
    ques_dict = {}
    ques_all_dict = {}
    all_ques = {}
    for i in range(len(level_detail)):
        level_no = level_detail[i].levels
        level_low = level_detail[i].reading_range_low
        level_high = level_detail[i].reading_range_high
        level_name = "Level " + str(level_no)
        level_range = str(level_high) + " - " + str(level_low)
        level_dict[level_name] = {"range": level_range}
        vocab_dict[level_name] = []
        ques_dict[level_name] = 0
        ques_all_dict[level_name] = [0,0,0,0]
    ques_all_dict["Total"] = [0,0,0,0]

    for i in range(len(vocab_detail)):
        level_no = vocab_detail[i].level.levels
        word = vocab_detail[i].word
        level_name = "Level " + str(level_no)
        vocab_dict[level_name].append(word)

    for i in range(len(ques_detail)):
        # print(ques_detail[i].question_text)
        # print(ques_detail[i].contact_time)
        level_no = ques_detail[i].level.levels
        question_type = ques_detail[i].question_category
        level_name = "Level " + str(level_no)
        ques_dict[level_name] += 1
        ques_all_dict[level_name][3] += 1
        ques_all_dict["Total"][3] += 1
        #
        cat = ["except","Comprehension","Vocabulary","Grammar"]
        gen = ["except","Politics","Sports","Science","Entertainment","World","Nation","Environment","Business","Tech","Lifestyle","Others"]
        #
        ind = i+1
        level_name = "Level " + str(ques_detail[i].level.levels)
        sub_skill = cat[int(ques_detail[i].question_category)]
        genre = gen[int(ques_detail[i].question_genre)]
        text = ques_detail[i].question_text
        all_ques["Question"+ str(ind)] = [ind, level_name, sub_skill, genre, text]
        if question_type == 1:
            ques_all_dict[level_name][0] += 1
            ques_all_dict["Total"][0] += 1
        elif question_type == 2:
            ques_all_dict[level_name][1] += 1
            ques_all_dict["Total"][1] += 1
        else:
            ques_all_dict[level_name][2] += 1
            ques_all_dict["Total"][2] += 1
    print (all_ques)
    context = {
        'level_range_detail': level_dict,
        'level_vocab_detail': vocab_dict,
        'level_ques_detail': ques_dict,
        'level_ques_all_detail':ques_all_dict,
        'all_ques':all_ques
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
        question_type = int(request.POST.get('question_type')[4])
        question_genre = int(request.POST.get('question_genre')[5])
        question_inst = request.POST.get('question_inst').strip()
        question_txt = request.POST.get('question_txt').strip()
        question_content = question_txt
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        option_choice = int(request.POST.get('option_choice'))
        print(request.POST.get('level_no'))
        level_no = int(request.POST.get('level_no'))
        level_detail = Level.objects.filter(Q(levels=level_no))[0]
        vocab_detail = LevelWords.objects.filter(Q(level=level_detail))
        all_vocab_detail = LevelWords.objects.filter(level__lt=level_detail)
        # print (all_vocab_detail[1].word)
        # print (11)
        all_vocab =[]
        cumulative_vocab =[]
        level_low = level_detail.reading_range_low
        level_high = level_detail.reading_range_high
        for i in range(len(vocab_detail)):
            all_vocab.append(vocab_detail[i].word)
        for i in range(len(all_vocab_detail)):
            cumulative_vocab.append(all_vocab_detail[i].word)
        score = textstat.flesch_reading_ease(question_txt)
        # print (question_txt)
        # print (score)
        text_with_pos_tag = nltk.word_tokenize(question_txt)
        question_all_vocab = nltk.pos_tag(text_with_pos_tag)
        question_vocab = []
        for i in range(len(question_all_vocab)):
            # print (question_all_vocab)
            word = question_all_vocab[i][0]
            pos_tag = question_all_vocab[i][1]
            if pos_tag in ["JJ","JJR","JJS","NN","NNS","RB","RBR","VB","VBD","VBG","VBZ"]:
                question_vocab.append(word.lower())
        all_vocab = all_vocab + cumulative_vocab
        for wor in question_vocab:
            if wor not in all_vocab:
                return JsonResponse({"main": "Question has not been added.", "body": "Please change this word " + wor}, safe=False)
        if score < level_low:
            return JsonResponse({"main": "Question has not been added.",
                                 "body": "Readability score is less than permissible" },
                                safe=False)
        try:
            LevelQuestion.objects.create(question_category=question_type, question_genre=question_genre, level=level_detail, question_inst=question_inst, question_text=question_txt, choice1=option1,
                                         choice2=option2, choice3=option3, choice4=option4,
                                         correct=option_choice, feedback="",date=today
                                         )

            return JsonResponse({"main": "Question has been added.", "body": question_content}, safe=False)
        except IntegrityError as e:
            print(e.args[0])
            print(828282)
            if 'UNIQUE constraint' in e.args[0]:
                print(9191191)
                return JsonResponse({"main": "Question has not been added.", "body": "Question text already exists."}, safe=False)
            else:
                return JsonResponse({"main": "Question has not been added.",
                                     "body":"Please check the question content again."},
                                    safe=False)

# immediate -
# forbidden
# all_questions vs Dash
#data



#requirements.txt
#add webserver - nginx, ?, mysql
#move to spacy, move to new ec2 instance, 16.04
# create data
#change questiion detail

#https://courses.edx.org/courses/course-v1:Microsoft+DEV287x+1T2018a/course/ - coursera Ml
#https



# verify, show error  - dependency - django 2.4, pip install textstat, spacy
# pip install -U spacy, python -m spacy download en

#vocab - http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization
# download wordnet
#use both if lemma change then go with it or go with stemming
#spacy


#move to react



# grammar - she?
# comprehension - ????