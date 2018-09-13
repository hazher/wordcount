
from django.http import HttpResponse
from django.shortcuts import render
import operator

#def home(request):
#    return HttpResponse('Home!')

def home(request):
    return render(request, 'home.html', {'key1': 'this is me'})

def eggs(request):
    return HttpResponse('eggs ARE GREATE!')

def count(request):
    '''
    count how many words in a text, and
    does an analysis words that repeat!
    '''
    fulltext = request.GET['fulltext']
    word_dict = {}
    for word in fulltext.split():
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word] = 1

    sortedWords = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    print('fulltext is: %a' % fulltext)
    return render(request, "count.html", {'fulltext': fulltext, 'wordcount': len(fulltext.split(' ')), 'word_dictionary': sortedWords})

def about(request):
    return render(request, "about.html")