from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterUserForm
# Create your views here.
def set(request):
    request.session['name'] = {'nam1':'simar','name2':'rahul'}
    request.session['fatherName'] = 'GOD'
    # request.session.set_expiry(5)
    return HttpResponse("Hello World")

def get(request):
    name = request.session['name']
    father_name = request.session['fatherName']
    # request.session['name'] = 'Rahul'
    print(name)
    print(father_name)
    print(request.session.get_expiry_age())
    return HttpResponse(f'<h1>GET VIEW</h1> {name}')

def delete(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse("<h1>Delete View</h1>")

def update(request):
    request.session['name']['nam1'] = 'John'
    request.session.modified = True
    return HttpResponse("update page")

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterUserForm()
    return render(request,'sessiontut/register.html',{'f':form})