from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
# Create your views here.

def Insert_Topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        fined_date=TopicForm(request.POST)
        if fined_date.is_valid():
            fined_date.save()
            return HttpResponse('The data inserted Successfully')
    return render(request,'Insert_Topic.html',d)