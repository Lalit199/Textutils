# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    extraspace=request.POST.get('extraspace','off')
    charcount=request.POST.get('charcount','off')


    if removepunc == "on" :
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newline=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n"and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'newlineremove', 'analyzed_text': analyzed}
        djtext = analyzed
    if (extraspace == 'on'):
        analyzed=""
        for char in range(len(djtext)):
            if djtext[char] ==" " and djtext[char+1] ==" ":
                pass
            else:
                analyzed=analyzed+djtext[char]
        params = {'purpose': 'extraspace remover', 'analyzed_text': analyzed}


    # if (charcount == 'on'):
    #     count=0
    #     for char in range(len(djtext)):
    #         if djtext[char] ==" " and djtext[char+1] ==" ":
    #             pass
    #         elif(djtext[char] ==" "):
    #             pass
    #         else:
    #             count+=1
    #     params = {'purpose': 'charcount', 'analyzed_text': count}



    if(removepunc!='on'and fullcaps!='on'and extraspace!='on'and newline!='on'and charcount!='on' ):
        params={'purpose':'nothing','analyzed_text':'please select a option'}
    return render(request, 'analyze.html', params)


