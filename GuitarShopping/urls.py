from django.urls import path
from . import views

#Method path takes 3 arguements
urlpatterns = [
    path('GuitarHome/', views.home, name='GuitarHome'),
    path('AddGuitar/', views.add_guitar, name='AddGuitar'),
    path('SeeChoices/', views.see_choices, name='SeeChoices'),
    path('GuitarDetails/<int:_id>', views.guitar_details, name='GuitarDetails'),
]