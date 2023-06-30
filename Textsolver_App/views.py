from django.shortcuts import render
from .models import Text

# Logic


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')




# Actions

def analyze(request):

    # Input
    text = request.POST.get('text', 'default')
    input_text = text
    # print(text)

    # Check Box Values Input
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    fulllow = request.POST.get('fulllow','off')

    # print(removepunc)

    analyzed = ""
    # Logic
    if removepunc == 'on':
        analyzed = ""
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''' 
        for char in text:
           if char not in punctuation:
                analyzed = analyzed + char
        text = analyzed        
    
    if fullcaps == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        text = analyzed

    if newlineremover == 'on':
        analyzed = ""
        analyzed = text.replace("\n","").replace("\r"," ")
        text = analyzed

    if fulllow == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.lower()
        text = analyzed
    
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(text):
           if not(text[index] == " " and text [index + 1 ] == " " ):
               analyzed = analyzed + char
        text = analyzed

    print(analyzed) 

    params = {'analyzed' : analyzed}

    # Instert in Database   

    model_text = Text(inp_text = input_text, output_text = text )
    model_text.save()
    return render(request, 'index.html' , params)