Live Project 

 

Introduction 

 

I participated in a two-week live project sprint along with my teammates to help build an overall project website. My particular task was to create a fully functioning application. I chose to create an application that would help a user who would be interested in shopping to buy themselves a new guitar. My application will help them research brands and models based on pricing. I used the programming language Python to help build the application. I also utilized the software program PyCharm to organize my code in an efficient matter. I am including some of my specific code to show the different pages within the application and the functions of the particular parts. 

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Guitar
from .forms import ShoppingForm



This is the views page that shows the different components of the application. It includes a form for the user to enter their possible options in order to help them make a decision on what guitar to buy.

def home(request):
    return render(request, 'GuitarShopping/home.html')


# Takes user to page where they can add a guitar to the database
def add_guitar(request):
    form = ShoppingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('GuitarHome')
    else:
        print(form.errors)
        messages.error(request, "Error")
    context = {'form': form}
    return render(request, "GuitarShopping/addGuitar.html", context)\

# Retrieves all choices for the guitar shopping application
def see_choices(request):
    all_guitars= Guitar.objects.all()
    context = {
        'all_guitars': all_guitars,
    }
    return render(request, "GuitarShopping/seeChoices.html", context)

# Retrieves one choice for a guitar purchase
def guitar_details(request,_id):

    guitar = Guitar.objects.get(id =_id)

    content = {
        'guitar': guitar,
    }
    return render(request, "GuitarShopping/guitarDetails.html", content)
    
    
This section of code will show the results of the user's entries from the shopping form.It will also include links that will take them to another page that will display a single option of their choice.

{% extends "GuitarShopping/base.html" %}

{% block title %}Guitar App - See Choices{% endblock %}

{% block header %}See Model Choices{% endblock %}

{% block content %}


{% for guitar in all_guitars %}
<a href="{% url 'GuitarDetails' guitar.id %}">Guitar Detail</a>
    <ul>
        <li><label><b>Brand Name: </label>{{guitar.brand_name}}</b></li>
        <li><label><b>Type: </label>{{guitar.instrument_type}}</b></li>
        <li><label><b>Model: </label>{{guitar.model_choice}}</b></li>
        <li><label><b>Price: </label>{{guitar.price}}</b></li>
    </ul>
{% endfor %}
 


