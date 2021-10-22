from django.shortcuts import render,redirect
from pizza.forms import PizzaForm
from .models import PizzaApp

# Create your views here.
def home(request):
    return render(request, "pizza/home.html")

def order(request):
    form = PizzaForm()
    
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    
    context = {
       
       "form":form     
    }
    
    return render(request, "pizza/order.html",context)

def order_list(request):
    orders = PizzaApp.objects.all()
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order")
    context = {
        'form':form,
        'orders' : orders,
    }
    return render(request, "pizza/order_list.html", context)
    