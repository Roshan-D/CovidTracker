from django.urls import path
from . import views

urlpatterns = [
    path('', views.selectCountry, name='SelectACountry'),
    path('graph/', views.graph, name='graph')
]
