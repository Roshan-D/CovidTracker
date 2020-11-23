from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Grapher, CountryForm


# Create your views here.
def selectCountry(request):
    form = CountryForm()
    return render(request, 'C:/Users/taged/PycharmProjects/CovidTracker/templates/form.html', {'form': form})


def graph(request):
    grapher = Grapher()
    canvas = grapher.my_figure(request.POST.get('country_model'))
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response