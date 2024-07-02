from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import CustomerProject
from accounts.models import CustomerAccount
from .forms import CustomerProjectForm

# Create your views here.

def customer_project_list_view(request):
    accounts = CustomerProject.objects.all()
    context = {'accounts': accounts}
    return render(request, 'projects/customer_projects_list_view.html', context=context)

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



def customer_project_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)

        form = CustomerProjectForm(request.POST)
        print(f"This is {request.POST.get('cp_name')}")
        
        if form.is_valid():
            account_name = form.cleaned_data.get('cp_name')
            print(f"account name: {account_name}")

            selected_account_id_for_customer_vendor = request.POST.get('cp_customer_vendor_uuid', None)
            selected_account_id_for_end_customer = request.POST.get('cp_end_customer_uuid', None)

            print(f"selected_account_id_for_customer_vendor {selected_account_id_for_customer_vendor}")
            
            if CustomerProject.objects.filter(cp_name=account_name).exists():
                form.add_error('cp_name', 'This account already exists.')
            
            else:
                new_account = form.save(commit=False)
                new_account.cp_customer_vendor_id = selected_account_id_for_customer_vendor
                new_account.cp_end_customer_id = selected_account_id_for_end_customer
                new_account.save()
                messages.success(request, 'Customer project created successfully.')
                return redirect('projects:customer_project_list_view')
                # return redirect('projects:customer_project_detail_view', pk=new_account.pk)
        
        else:
            print(form.errors)
    
    else:
        form = CustomerProjectForm()
    # return render(request, 'projects/test.html', {'form': form})
    return render(request, 'projects/customer_project_creation_form.html', {'form': form})


def customer_account_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerAccount.objects.filter(ca_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.ca_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

def customer_project_detail_view(request, pk):
    print(pk)
    customer_project = CustomerProject.objects.filter(pk=pk).first()
    context = {'customer_project': customer_project}
    return render(request, 'projects/customer_project_detail_view.html', context=context)


def customer_project_edit_form(request, pk=None):
    if pk:
        account = get_object_or_404(CustomerProject, pk=pk)
    else:
        account = None

    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)

        form = CustomerProjectForm(request.POST, instance=account)
        print(f"This is {request.POST.get('cp_name')}")
        
        if form.is_valid():
            account_name = form.cleaned_data.get('cp_name')
            print(f"account name: {account_name}")

            selected_account_id_for_customer_vendor = request.POST.get('cp_customer_vendor_uuid', None)
            selected_account_id_for_end_customer = request.POST.get('cp_end_customer_uuid', None)

            print(f"selected_account_id_for_customer_vendor {selected_account_id_for_customer_vendor}")
            
            if CustomerProject.objects.filter(cp_name=account_name).exclude(pk=pk).exists():
                form.add_error('cp_name', 'This project name already exists.')
            else:
                account = form.save(commit=False)
                account.cp_customer_vendor_id = selected_account_id_for_customer_vendor
                account.cp_end_customer_id = selected_account_id_for_end_customer
                account.save()

                if pk:
                    messages.success(request, 'Customer project updated successfully.')
                else:
                    messages.success(request, 'Customer project created successfully.')
                
                return redirect('projects:customer_project_list_view')
        else:
            print(form.errors)
    else:
        print(account.cp_customer_vendor)
        cp_customer_vendor_uuid = CustomerAccount.objects.filter(ca_name=account.cp_customer_vendor).values_list('pk', flat=True).first()
        print(cp_customer_vendor_uuid)
        cp_end_customer_uuid = CustomerAccount.objects.filter(ca_name=account.cp_end_customer).values_list('pk', flat=True).first()
        print(cp_end_customer_uuid)
        print(account)
        account.cp_customer_vendor_uuid = cp_customer_vendor_uuid
        account.cp_end_customer_uuid = cp_end_customer_uuid
        form = CustomerProjectForm(instance=account)

    return render(request, 'projects/customer_project_edit_form.html', {'form': form, 'account': account})
