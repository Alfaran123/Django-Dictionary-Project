from os import symlink
from django.shortcuts import redirect, render
from PyDictionary import PyDictionary
from .models import Dictionary
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')


def meaning(request):

    Search=request.POST['search']
    dictionary=PyDictionary()
    meaning=dictionary.meaning(Search)

    

    if Dictionary.objects.filter(word=Search).exists():
            
        context={
        'meaning':meaning
        }
        return render(request,'word.html',context)
    else:
        context={
        'meaning':meaning
        }
        Word=Dictionary.objects.create(word=Search,meaning=meaning)
        Word.save();
    return render(request,'word.html',context)
    
    