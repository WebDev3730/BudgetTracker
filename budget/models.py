from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Transaction_Types = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    category_types = [
        ('food', 'Food'),
        ('Enterntainment', 'Entertainment'),
        ('Utility', 'Utility'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=category_types)
    transaction_type = models.CharField(max_length=7, choices=Transaction_Types)
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.name