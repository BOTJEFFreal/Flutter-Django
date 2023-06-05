from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people =[
        {'name':"Akshay",'age':'10'},
        {'name':"Roy",'age':'15'},
        {'name':"Ram",'age':'20'},
    ]
    return(render(request,'home/index.html',context={'people':people}))
