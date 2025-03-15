from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import TodoForm
from .models import Todos
from django.views.generic.base import RedirectView,TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
def home(request):
    return render(request,'Hello World!')

# class HomeView(View):
#     def get(self,request):
#         #get request
#         todo = Todos.objects.all()
#         return render(request,"todo/index.html",{'todos':todo})

class HomeView(ListView):
    model = Todos
    ordering = ['-id']
    template_name = 'todo/index.html'
    context_object_name = 'todos'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = 'simar'
    #     return context

    # def get_queryset(self):
    #     return Todos.objects.filter(todo__icontains='s')

def details(request,id):
    todo = Todos.objects.get(id=id)
    return render(request,'todo/detail.html',{'todo':todo})

class DetailView(DetailView):
    model = Todos
    template_name = 'todo/detail.html'
    context_object_name = 'todo'

# class AddView(View):
#     def get(self,request):
#         form = TodoForm()
#         return render(request,'todo/add.html',{'form':form})
    
#     def post(self,request):
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         return render(request,'todo/add.html',{'form':form})

# class AddView(FormView):
#     template_name = 'todo/add.html'
#     form_class = TodoForm
#     success_url = '/'

#     def form_valid(self,form):
#         print(form.cleaned_data['todo'])
#         form.save()
        
#         return super().form_valid(form)

class AddView(CreateView):
    # model = Todos
    # fields = '__all__'
    form_class = TodoForm
    success_url = '/'
    template_name = 'todo/todos_add.html'
    # template_name_suffix = '_add'

class UpdateTodoView(UpdateView):
    model = Todos
    # fields= "__all__"
    form_class = TodoForm
    template_name = 'todo/todos_add.html'
    # template_name_suffix = '_add'
    success_url = '/'

class DeleteTodoView(DeleteView):
    model = Todos
    success_url = '/'


class AboutView(TemplateView):
    template_name = 'todo/about.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context['CompanyName'] = 'Taranjot Singh'
        return context
    
class RedirectAbout(RedirectView):
    pattern_name = 'home'
    query_string = True