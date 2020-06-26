from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fullText = request.GET['fullText']

    wordList = fullText.split()
    characterCount = len(fullText)

    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedDict = sorted(wordDictionary.items() , key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{ 
        'fulltext' : fullText,
        'wordList' : len(wordList),
        'TotalChar': characterCount,
        'wordDictionary' : sortedDict  
        })

def about(request):
    return render(request , 'about.html')