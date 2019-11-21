from django.shortcuts import render, render, HttpResponse
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Question, Choice
import json
from django.views.decorators.csrf import csrf_exempt

# list view for poll
@csrf_exempt
def index(request):
    result = Choice.objects.all().\
        values('id','choice_text','question_id','question__question_text','question__pub_date','votes').\
        order_by('question_id')
    data = []
    selected_question_id = None
    tmp = None
    for item in result:
        # here we are grouping the question and its options
        if selected_question_id == item['question_id']:
            tmp['options'].append({'choice_id' :item['id'], 'choice': item['choice_text'], 'votes': item['votes']})
        else:
            selected_question_id = item['question_id']
            if tmp:
                data.append(tmp)
            # creating a temporary variable
            tmp = {
                'id': item['question_id'],
                'question_text': item['question__question_text'],
                'pub_date': item['question__pub_date'],
                'options': [{'choice_id' :item['id'], 'choice': item['choice_text'], 'votes': item['votes']}]
            }
    if tmp:
                data.append(tmp)
    context = {
        'data': data,
        'message': 'msg'
    }
    return JsonResponse(context)

@csrf_exempt
def vote(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data:
            id_list = list(data.values())
            # voting for specific choices
            objects = Choice.objects.filter(id__in=id_list)
            for obj in objects:
                obj.votes += 1
                obj.save()
        return JsonResponse({'status':'success'})
    return not_implimented()

# for creating a question
@csrf_exempt
def add_question(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            obj = Question()
            obj.question_text=data['question_text']
            obj.pub_date=data['pub_date']
            obj.save()

            for item in data['choices']:
                obj2 = Choice()
                obj2.question = obj
                obj2.choice_text = item
                obj2.save()

            return JsonResponse({
                'status': 'success', 
                'message': 'Question added successfull'})

        except IntegrityError as e:
            return JsonResponse({
                'status': 'failed', 
                'message': 'Question already exist'})
    return not_implimented()

def not_implimented():
    return JsonResponse({
                'status': 'failed', 
                'message': 'This method not implimented yet'})