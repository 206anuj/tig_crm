from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse

from .models import FteSerivce
from .forms import FteServiceForm

from projects.models import CustomerProject, VendorProject
from accounts.models import VendorAccount
from project_site.models import ProjectSite
from orders.models import SalesOrder
# Create your views here.

def services_list_view(request):
    fte_services = FteSerivce.objects.all()
    context = {'fte_services': fte_services}
    return render(request, 'services/services_list_view.html', context=context)


@require_POST
def select_account_type(request):
    service_type = request.POST.get('account_type')
    if service_type in ['AMC', 'Dispatch', 'FTE', 'Fixed Feed', 'Migration', 'Schedule Visit', 'Indirect Expense', 'FTE OT']:
        if service_type == 'FTE':
            print(service_type)
            return redirect('services:fte_service_creation_form')
        # elif account_type == 'vendor':
        #     return redirect('accounts:vendor_account_creation_form')
    else:
        return render(request, 'select_account_type.html', {'error': 'Invalid account type selection'})
    


    # if request.method == 'POST':
    #     all_post_data = request.POST
    #     print("All POST data:", all_post_data)

def fte_service_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)
        form = FteServiceForm(request.POST)
        if form.is_valid():
            fte_services_name = form.cleaned_data.get('fte_serivce_name')

            selected_customer_project_id = request.POST.get('fte_serivce_project_uuid', None)
            selected_project_site_id = request.POST.get('fte_serivce_project_site_uuid', None)
            selected_sales_order_id = request.POST.get('fte_serivce_customer_purchase_order_uuid', None)
            selected_vendor_account_id = request.POST.get('fte_serivce_vendor_name_uuid', None)
            selected_vendor_project_id = request.POST.get('fte_serivce_vendor_project_uuid', None)
            print(f"Ids: {selected_customer_project_id, selected_project_site_id, selected_sales_order_id, selected_vendor_account_id, selected_vendor_project_id }")
            if FteSerivce.objects.filter(fte_serivce_name=fte_services_name).exists():
                form.add_error('fte_serivce_name', 'This service already exists.')
            else:
                new_fte_service = form.save(commit=False)
                new_fte_service.fte_serivce_project_id = selected_customer_project_id
                new_fte_service.fte_serivce_project_site_id = selected_project_site_id
                new_fte_service.fte_serivce_customer_purchase_order_id = selected_sales_order_id
                new_fte_service.fte_serivce_vendor_name_id = selected_vendor_account_id 
                new_fte_service.fte_serivce_vendor_project_id = selected_vendor_project_id

                new_fte_service.save()
                messages.success(request, 'Sales Order created successfully.')
                return redirect('services:services_list_view')
        else:
            print(form.errors)
    else:
        form = FteServiceForm()
    return render(request, 'services/fte_service_creation_form.html', {'form': form})


def fte_service_detail_view(request, pk):
    fte_service = FteSerivce.objects.filter(pk=pk).first()
    context = {'fte_service': fte_service}
    return render(request, 'services/fte_service_detail_view.html', context=context)


def customer_project_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerProject.objects.filter(cp_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.cp_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})


def project_site_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = ProjectSite.objects.filter(ps_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.ps_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

def sales_order_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = SalesOrder.objects.filter(so_po_number__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.so_po_number} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

def vendor_account_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = VendorAccount.objects.filter(va_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.va_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

def vendor_project_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = VendorProject.objects.filter(vp_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.vp_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})