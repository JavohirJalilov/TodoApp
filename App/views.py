from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def read(request):
	data = open('todo.json').read()
	return 	HttpResponse(data)

def add(request):
	data = json.loads(open('todo.json').read())
	count = data['count']+1
	task = request.GET.get('task')
	data[count] = task
	data['count'] = count
	f = open('todo.json','w')
	f.write(json.dumps(data))
	return HttpResponse('To add: task = task')

def delete(request):
	data = json.loads(open('todo.json').read())
	key = request.GET.get('key')
	del data[key]
	f = open('todo.json','w')
	f.write(json.dumps(data))
	return HttpResponse('Enter the task key to disable, example: key=2')

