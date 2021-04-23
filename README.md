Live Project 

 

Introduction 

Guitar Shopping Application

 

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

C# Live Project

I worked as part of a team to update a theater company's website in order to make it more efficient and attractive to potential customers. As part of these overall goals, 
I created a blog authors section that could highlight a professional reviewer's comments in blog form to promote performances at the theater.

1. Created a blog authors index page

This provided a method to save  a blog author's information on a bootstrap card  and save it to the
blog author's page.

@model IEnumerable<TheatreCMS3.Areas.Blog.Models.BlogAuthor>

@{
    ViewBag.Title = "Index";
}
<script src="https://kit.fontawesome.com/14a23f6393.js" crossorigin="anonymous"></script>

<h2>Index</h2>

<p>
    @Html.ActionLink("Create New", "Create")
    
</p>

@foreach (var blogAuthor in Model)
{


    <div class="card mb-4">
        <div class="row no-gutters">
            <div class="col-auto">
                <a href="https://placeholder.com"><img src="https://via.placeholder.com/150" class="img-fluid" alt="Blog Author"></a>
            </div>
            <div class="col">
                <div class="blogAuthor-Card text-left">
                    <p class="card-text">
                        Author for Theater Vertigo<br />
                        <b>@blogAuthor.Name</b><br />@blogAuthor.Name @blogAuthor.Bio
                    </p>
                </div>
                
                
 2. Another task I completed was to use a button that is responsive to a user to see information about a blog author
 and even delete a blog author if so desired by the theater.
 
 <div>
                    <a href="@Url.Action("Edit")" class="btn btn-edit float-left">
                        <i class="fas fa-theater-masks"></i>Edit
                    </a>

                </div>
                <div>
                    <a href="@Url.Action("Details", new { id=blogAuthor.BlogAuthorid} )" class="btn btn-details float-left">
                        <i class="fas fa-theater-masks"></i>Details
                    </a>

                </div>
                <div>
                    <a href="@Url.Action("Delete", new { id = blogAuthor.BlogAuthorid })" class="btn btn-delete float-right">
                        <i class="fas fa-theater-masks"></i>Delete
                    </a>


                </div>


            </div>
            
            @model TheatreCMS3.Areas.Blog.Models.BlogAuthor

@{
    ViewBag.Title = "Details";
}

<script src="https://kit.fontawesome.com/14a23f6393.js" crossorigin="anonymous"></script>


<h2>Details</h2>
<h4>BlogAuthor</h4>
<hr />

<div>
    <button type="button" class="btn btn-authDetails position-relative">Author Details</button>
    <button onclick="displayCard()" type="button" class="btn btn-latePosts position-relative">Latest Posts</button>
    <button type="button" class="btn btn-contact position-relative">Contact</button>
    <button type="button" class="btn btn-twitter position-relative">Twitter</button>
    
</div>


 


