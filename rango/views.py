from pydoc import html
from re import A
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by <your-name>.'}
    return render(request, 'rango/about.html',context=context_dict)

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!

    #queries the Category model to retrieve the top five categories
    category_list = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)