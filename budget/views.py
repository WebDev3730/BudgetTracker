from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Transaction
from django.contrib.auth import login, logout, authenticate
from .forms import TransactionForm, RegistrationForm, EditTransactionForm, TransactionFilterForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    else:
        transactions = Transaction.objects.filter(user=request.user)
        total_income = transactions.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
        total_expenses = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
        balance = total_income - total_expenses

    if 'clear_filters' in request.GET:
        form = TransactionFilterForm()  # Create a blank form
    

    else:    
        form = TransactionFilterForm(request.GET or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            category = form.cleaned_data.get('category')
            transaction_type = form.cleaned_data.get('transaction_type')
            amount = form.cleaned_data.get('amount')
            

            if start_date:
                transactions = transactions.filter(date__gte=start_date)
            if end_date:
                transactions = transactions.filter(date__lte=end_date)
            if category:
                transactions = transactions.filter(category=category)
            if transaction_type:
                transactions = transactions.filter(transaction_type=transaction_type)
            if name:
                transactions = transactions.filter(name=name)
            if amount:
                transactions = transactions.filter(amount=amount)
            
        
    

    return render(request, 'home.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'form': form,
    })


def AddTransaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Transaction Added")
            return redirect('home')
    else:
        form = TransactionForm()

    return render(request, 'add_transaction.html', {'form': form})

def customer_transactions(request, pk):
    if request.user_is_authenticated:
        customer_transactions = get_object_or_404(Transaction, id=pk, user=request.user)
        return render(request, 'home.html', {'customer_transactions': customer_transactions})
    else: 
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Created')
            return redirect('login') 
        else: 
            messages.success(request, 'There Was An error, Please Try Again')
            return redirect('register')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})


def EditTransaction(request, pk):
    transaction = get_object_or_404(Transaction, id=pk, user=request.user)
    if request.method == 'POST':
        form = EditTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Made Successfully')
            return redirect('home')
    else:
        form = EditTransactionForm(instance=transaction)
    
    return render(request, 'edit_transaction.html', {'form': form})

def DeleteTransaction(request, pk):
    transaction = get_object_or_404(Transaction, id=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction Deleted')
        return redirect('home')
    
    return render(request, 'delete_transaction.html', {'transaction': transaction})

def logout_user(request):
    logout(request)
    return redirect('home')
