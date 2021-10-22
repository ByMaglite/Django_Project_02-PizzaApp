from django import forms
from .models import PizzaApp


class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaApp
        fields = '__all__'
        labels = {'topping1':'Topping 1:','topping2':'Topping 2:', 'size':'Size:'}
    
     
# class TodoUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ["title", "completed"]