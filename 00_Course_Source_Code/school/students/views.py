from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
def set(request):
    # raise Exception("Set raises an exception")
    print('set view is called')
    response =  TemplateResponse(request,"students/home.html",{'name':'tarnjot'})
    response.set_cookie('theme','dark',httponly=True)
    response.set_cookie("name",'Rahul')
    return response

def get(request):
    print(request)
    theme = request.COOKIES['theme']
    return HttpResponse(f"<h1>GET</h1> {theme}")

def delete(request):

    response =  HttpResponse("Deleted")
    response.delete_cookie("name")
    return response

def update(request):
    response = HttpResponse('<h1>Updated</h1>')
    response.set_cookie('name','Simar')
    return response