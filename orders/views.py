from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import SalesOrder
from accounts.models import CustomerAccount
from projects.models import CustomerProject
from .forms import SalesOrderForm

# Create your views here.

def sales_order_list_view(request):
    sales_order = SalesOrder.objects.all()
    context = {'sales_order': sales_order}
    return render(request, 'orders/sales_order_list_view.html', context=context)

def sales_order_detail_view(request, pk):
    sales_order = SalesOrder.objects.filter(pk=pk).first()
    context = {'sales_order': sales_order}
    return render(request, 'orders/sales_order_detail_view.html', context=context)

@require_POST
def select_account_type(request):
    account_type = request.POST.get('account_type')
    if account_type in ['customer', 'vendor']:
        if account_type == 'customer':
            return redirect('accounts:customer_account_creation')
        elif account_type == 'vendor':
            return redirect('accounts:vendor_account_creation')
    else:
        return render(request, 'select_account_type.html', {'error': 'Invalid account type selection'})


def sales_order_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)

        form = SalesOrderForm(request.POST)
        print(f"This is {request.POST.get('so_po_number')}")
        
        if form.is_valid():
            account_name = form.cleaned_data.get('so_po_number')
            print(f"account name: {account_name}")

            selected_account_id_for_customer_vendor = request.POST.get('so_customer_vendor_uuid', None)
            selected_account_id_for_project = request.POST.get('so_project_uuid', None)

            print(f"selected_account_id_for_customer_vendor {selected_account_id_for_customer_vendor}")
            
            if SalesOrder.objects.filter(so_po_number=account_name).exists():
                form.add_error('cp_name', 'This account already exists.')
            
            else:
                new_account = form.save(commit=False)
                new_account.so_customer_vendor_id = selected_account_id_for_customer_vendor
                new_account.so_project_id = selected_account_id_for_project
                new_account.save()
                messages.success(request, 'Sales Order created successfully.')
                return redirect('orders:sales_order_list_view')
        
        else:
            print(form.errors)
    
    else:
        form = SalesOrderForm()
    # return render(request, 'projects/test.html', {'form': form})
    return render(request, 'orders/sales_order_creation_form.html', {'form': form})


def customer_account_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerAccount.objects.filter(ca_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.ca_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

def customer_project_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerProject.objects.filter(cp_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.cp_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})


def sales_order_edit_form(request, pk):
    if pk:
        account = get_object_or_404(SalesOrder, pk=pk)
    else:
        account = None

    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)

        form = SalesOrderForm(request.POST, instance=account)
        print(f"This is {request.POST.get('so_po_number')}")

        if form.is_valid():
            account_name = form.cleaned_data.get('so_po_number')
            print(f"Account name: {account_name}")

            selected_account_id_for_customer_vendor = form.cleaned_data.get('so_customer_vendor_uuid')
            selected_account_id_for_project = form.cleaned_data.get('so_project_uuid')

            print(f"Selected account ID for customer/vendor: {selected_account_id_for_customer_vendor}")
            print(f"Selected account ID for project: {selected_account_id_for_project}")

            if SalesOrder.objects.filter(so_po_number=account_name).exclude(pk=pk).exists():
                form.add_error('so_po_number', 'This Sales Order already exists.')
            else:
                account = form.save(commit=False)
                account.cp_customer_vendor_uuid = selected_account_id_for_customer_vendor
                account.cp_customer_vendor = CustomerAccount.objects.get(id=selected_account_id_for_customer_vendor)
                account.cp_project_uuid = selected_account_id_for_project
                account.cp_project = CustomerProject.objects.get(id=selected_account_id_for_project)
                account.save()

                if pk:
                    messages.success(request, 'Sales Order updated successfully.')
                else:
                    messages.success(request, 'Sales Order created successfully.')

                return redirect('orders:sales_order_list_view')
        else:
            print(form.errors)
    else:
        if account:
            so_customer_vendor_uuid = CustomerAccount.objects.filter(ca_name=account.so_customer_vendor).values_list('pk', flat=True).first()
            so_project_uuid = CustomerProject.objects.filter(cp_name=account.so_project).values_list('pk', flat=True).first()
            account.so_customer_vendor_uuid = so_customer_vendor_uuid
            account.so_project_uuid = so_project_uuid
            form = SalesOrderForm(instance=account)
        else:
            form = SalesOrderForm()

    return render(request, 'orders/sales_order_edit_form.html', {'form': form, 'account': account})
