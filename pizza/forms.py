from django import forms
from .models import PizzaApp


class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaApp
        fields = '__all__'
     
# class TodoUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ["title", "completed"]