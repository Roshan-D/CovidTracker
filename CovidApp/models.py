from django.db import models
from django.forms import ModelForm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from os.path import expanduser as ospath


# Create your models here.
class Grapher():
    def my_figure(self, thiscountry):
        country = thiscountry

        df = pd.read_excel(ospath('C:/Users/taged/PycharmProjects/CovidTracker/CovidApp/total_cases.xlsx'),
                           'total_cases')
        x = df['date']
        y = df[country].divide(1000000)
        labels = []
        for i in range(1, len(df['date'])):
            if df['date'][i].month not in labels:
                labels.append(df['date'][i].month)

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        ax.plot(x, y, color='r')
        ax.set_title('Covid 19 Cases in ' + country)
        ax.set_xlabel('Month (mm)')
        ax.set_ylabel('Number of cases (x1e6)')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(color='gray', linestyle='-', linewidth=0.25, alpha=0.5)
        ax.set_xticklabels(labels)
        return canvas


class SelectCountry(models.Model):
    df = pd.read_excel(ospath('C:/Users/taged/PycharmProjects/CovidTracker/CovidApp/total_cases.xlsx'), 'total_cases')
    country_names = {}
    for entry in df[0:1]:
        country_names[entry] = entry
    country_list = [(k, v) for k, v in country_names.items()]
    COUNTRY_CHOICES = tuple(country_list[1:])

    country_model = models.CharField(max_length=50, choices=COUNTRY_CHOICES)


class CountryForm(ModelForm):
    class Meta:
        model = SelectCountry
        fields = ['country_model']