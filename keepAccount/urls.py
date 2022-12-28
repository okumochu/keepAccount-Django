from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search,name='search'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    path('graph',views.graph,name='graph'),
    path('generateCSV',views.generateCSV,name='generateCSV'),
    path('overview',views.overview,name='overview'),
]