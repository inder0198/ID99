from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.views.generic import TemplateView


class home(TemplateView):
    template_name = 'home.html'


# class add(TemplateView):
#     template_name = 'add.html'
#
#
# class display(TemplateView):
#     template_name = 'display.html'


def add(request):
    if request.method=="POST":
        form= BlogPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BlogPost()
        return render(request, 'add.html', {'form':form})


def display(request):
    data = Post.objects.all()
    return render(request, 'display.html', {'data': data})