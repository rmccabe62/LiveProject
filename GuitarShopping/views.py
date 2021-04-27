from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Guitar
from .forms import ShoppingForm




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









