from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('landing', views.landing),
    path('range', views.range),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    #path('', views.pie_chart, name='pie-chart'),
]
