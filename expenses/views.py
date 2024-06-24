from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Category, Expense
from django.contrib import messages
# Create your views here.

@login_required(login_url='/authentication/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def index(request):
    categories = Category.objects.all()
    return render(request, 'expenses/index.html')

@login_required(login_url='/authentication/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def add_expense(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        # validate amount input
        amount = request.POST['amount']
        # import pdb
        # pdb.set_trace()
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)
        
        # validate description input
        description = request.POST['description']
        # import pdb
        # pdb.set_trace()
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/add_expense.html', context)
        
        # category selection
        category = request.POST['category']

        # date input
        date = request.POST['expense_date']

        # owner input should also be passed

        Expense.objects.create(owner=request.user, amount=amount, date=date,
                               category=category, description=description)
        
        messages.success(request, 'Expense saved successfully')
        return redirect('expenses')
        