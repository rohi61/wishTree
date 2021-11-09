from django.shortcuts import render
from main.forms import groop_register_form, index_form



def index(request):
    
    form = index_form()

    context = {
        'form':form
    } 

    return render(request,'main/index.html',context)

def groop_register(request):

    form = groop_register_form()

    context = {
        'form':form
    } 

    return render(request,'main/groop_register.html',context)