from django import forms
from .models import Transaction, User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView, DeleteView

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'amount', 'category', 'transaction_type', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose One'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose a Category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a description of your Income/Expense...'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }

        labels = {
            'name': '',
            'amount': '',
            'description': '',
        }

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password Again'}),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),

        }
        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',

        }

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'amount', 'category', 'transaction_type', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DeleteTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'amount', 'category', 'transaction_type', 'description',)
        

class TransactionFilterForm(forms.ModelForm):
    name = forms.CharField(required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    amount = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    
    category = forms.ChoiceField(
        required=False,
        choices= [('', 'All Categories')] + Transaction.category_types,
    )
    transaction_type = forms.ChoiceField(
        required=False,
        choices= [('', 'All Types'), ('income', 'Income'), ('expense', 'Expense')],
    )
    
    class Meta:
        model = Transaction
        fields = ('name', 'category', 'transaction_type')