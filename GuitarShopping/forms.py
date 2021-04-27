from django.forms import ModelForm
from .models import Guitar

# # GUITAR_CHOICES = [
# #     ('FENDER', 'Fender'),
# #     ('GIBSON', 'Gibson'),
# ]

class ShoppingForm(ModelForm):
    class Meta:
        model = Guitar
        fields = '__all__'
