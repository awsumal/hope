# -*- encoding: utf-8 -*-

from aiohttp import request
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from json import dumps

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def landing(self):

    html_template = loader.get_template('home/landing.html')
    return HttpResponse(html_template.render())

'''
def pie_chart(request):
    labels = ["a","b","c","d","e"]
    data = [100,200,120,230,123]

    return render(request, 'index.html', {
        'labels': labels,
        'data': data,
    })'''


def population_chart(request):
    labels = ["a","b","c","d","e","f","g","h"]
    data1 = [100,200,120,230,123,100,123,235]

    ''' queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])'''
    context = {
        'labels': ["a","b","c","d","e","f","g","h"],
        'data': [100,200,120,230,123,100,123,235],
    }
    return render(request, 'home/index.html', context)