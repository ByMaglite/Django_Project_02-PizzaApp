from django.db import models

# Create your models here.

class PizzaApp(models.Model):
    topping1 = models.CharField( max_length=100)
    topping2 = models.CharField( max_length=100)
    SIZE =(
        ("Small", "küçük"),
        ("Medium", "orta"),
        ("Large", "büyük"),
    )
    size = models.CharField(max_length=50, choices=SIZE)
    
            
    def __str__(self):
        return f" Your pizzas prepared with {self.topping1} and {self.topping2} as {self.size}"
