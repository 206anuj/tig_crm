from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
 
from .models import CustomerProject, VendorProject
from accounts.models import CustomerAccount, VendorAccount
from .forms import CustomerProjectForm, VendorProjectForm
 
# Create your views here.
 
# @login_required
def customer_project_list_view(request):
    accounts = list(CustomerProject.objects.all())
    vendorProjects = list(VendorProject.objects.all())
    projects = accounts + vendorProjects
    projects = sorted( accounts + vendorProjects , key=lambda x: x.updated_at, reverse=True)
    context = {'projects' : projects}
    return render(request, 'projects/customer_projects_list_view.html', context=context)
 
# @login_required 
@require_POST
def select_project_type(request):
    project_type = request.POST.get('project_type')
    if project_type in ['customer', 'vendor']:
        if project_type == 'customer':
            return redirect('projects:customer_project_creation_form')
        elif project_type == 'vendor':
            return redirect('projects:vendor_project_creation_form')
    else:
        return render(request, 'projects:customer_project_list_view', {'error': 'Invalid account type selection'})
 
# customer projects views

# @login_required 
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


# @login_required
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
 
 
# vendor project view
# @login_required 
def vendor_project_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print('ALL POST DATA:', all_post_data)
 
        form = VendorProjectForm(request.POST)
        print(f"This is {request.POST.get('vp_name')}")
 
        if form.is_valid():
            project_name = form.cleaned_data.get('vp_name')
            print(f"project name: {project_name}")
 
            selected_account_id_for_vendor_account = request.POST.get('vp_vendor_account_uuid', None)
            selected_account_id_for_customer_project = request.POST.get('vp_customer_project_uuid', None)
 
            print(f"selected_account_id_for_vendor_account {selected_account_id_for_vendor_account}")
            print(f"selected_account_id_for_customer_project {selected_account_id_for_customer_project}")
 
            if VendorProject.objects.filter(vp_name = project_name).exists():
                form.add_error('vp_name', 'This account already exists.')
            else:
                new_v_project =  form.save(commit=False)
                new_v_project.vp_vendor_account_id = selected_account_id_for_vendor_account
                new_v_project.vp_customer_project_id = selected_account_id_for_customer_project
                new_v_project.save()
                messages.success(request, 'Customer project created successfully.')
                return redirect('projects:customer_project_list_view')  # Redirect to success page
        else:
            print(form.errors)
    else:
        form = VendorProjectForm()
   
    return render(request, 'projects/vendor_project_creation_form.html', {'form': form})
 
 
def vendor_account_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = VendorAccount.objects.filter(va_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.va_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})
 
 
def customer_project_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerProject.objects.filter(cp_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.cp_name} for account in accounts]
        # print(suggestions)
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})
 
# @login_required 
def vendor_project_detail_view(request, pk):
    print(pk)
    vendor_project = VendorProject.objects.filter(pk=pk).first()
    context = {'vendor_project': vendor_project}
    return render(request, 'projects/vendor_project_detail_view.html', context=context)
 
# @login_required 
def vendor_project_edit_form(request, pk=None):
    if pk:
        project = get_object_or_404(VendorProject, pk=pk)
    else:
        project = None
 
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)
 
        form = VendorProjectForm(request.POST, instance=project)
        print(f"This is {request.POST.get('vp_name')}")
       
        if form.is_valid():
            project_name = form.cleaned_data.get('vp_name')
            print(f"project name: {project_name}")
 
            selected_account_id_for_vendor_account = request.POST.get('vp_vendor_account_uuid', None)
            selected_account_id_for_customer_project = request.POST.get('vp_customer_project_uuid', None)
 
            if VendorProject.objects.filter(vp_name=project_name).exclude(pk=pk).exists():
                form.add_error('vp_name', 'This project name already exists.')
            else:
                project = form.save(commit=False)
                project.vp_vendor_account_id = selected_account_id_for_vendor_account
                project.vp_customer_project_id = selected_account_id_for_customer_project
                project.save()
 
                if pk:
                    messages.success(request, 'Vendor project updated successfully.')
                else:
                    messages.success(request, 'Vendor project created successfully.')
               
                return redirect('projects:customer_project_list_view')
        else:
            print(form.errors)
    else:
        print(project.vp_vendor_account)
        vp_vendor_account_uuid = VendorAccount.objects.filter(va_name=project.vp_vendor_account).values_list('pk', flat=True).first()
        print(vp_vendor_account_uuid)
        vp_customer_project_uuid = CustomerProject.objects.filter(cp_name=project.vp_customer_project).values_list('pk', flat=True).first()
        print(vp_customer_project_uuid)
        print(project)
        project.vp_vendor_account_uuid = vp_vendor_account_uuid
        project.vp_customer_project_uuid = vp_customer_project_uuid
        form = VendorProjectForm(instance=project)
 
    return render(request, 'projects/vendor_project_edit_form.html', {'form': form, 'project': project})