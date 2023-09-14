# Live Project 

 

## Introduction 

The following is an internship that I participated in that involved in upgrading a local theater group's website.

## [C# Live Project](https://github.com/rmccabe62/LiveProject/blob/master/TheaterCMS/TheatreCMS3/Views/Home/About.cshtml)

I worked as part of a team to update a theater company's website in order to make it more efficient and attractive to potential customers. As part of these overall goals, 
I created a blog authors section that could highlight a professional reviewer's comments in blog form to promote performances at the theater.

1. Created an about page giving the theater's information such as casting information for performances.

2. Created a blog authors index page

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
                
                
 3. Another task I completed was to use a button that is responsive to a user to see information about a blog author
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


 


