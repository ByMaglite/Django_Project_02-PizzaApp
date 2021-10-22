from django.db import models

# Create your models here.

class PizzaApp(models.Model):
    topping1 = models.CharField( max_length=100)
    topping2 = models.CharField( max_length=100)
    SIZE =(
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    )
    size = models.CharField(max_length=50, choices=SIZE)
    
            
    def __str__(self):
        return f" Topping 1: {self.topping1} , Topping 2: {self.topping2} , Size: {self.size}"
