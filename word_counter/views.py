from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

from django.http import HttpResponseRedirect
from .forms import NameForm



def HomePageView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url_1 = request.POST.get('your_url')
            print(url_1)
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            return HttpResponse("Datos URL:{}".format(url_1))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'word_counter/home.html', {'form': form})

