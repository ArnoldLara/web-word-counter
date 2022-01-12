from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

from django.http import HttpResponseRedirect
from .forms import NameForm
# Count words libraries
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation



def HomePageView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url_text = request.POST.get('your_url')
            print(url_text)
            # We get the url
            r = requests.get(url_text)
            soup=BeautifulSoup(r.text,'html.parser')

            # We get the words within paragrphs
            text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
            c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))
            
            # We get the words within divs
            text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
            c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))


            # We sum the two countesr and get a list with words count from most to less common
            #total = c_div + c_p
            total = c_p
            list_most_common_words = total.most_common(10) 
            print(list_most_common_words)
            
            return HttpResponse("10 Palabras más repetidas:{}".format(list_most_common_words))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'word_counter/home.html', {'form': form})

