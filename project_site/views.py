from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse


from .models import ProjectSite
from projects.models import CustomerProject
from .forms import ProjectSiteForm
# Create your views here.

# @login_required
def project_site_list_view(request):
    project_sites = ProjectSite.objects.all()
    context = {'project_sites': project_sites}
    return render(request, 'project_site/project_site_list_view.html', context=context)

# @login_required
def project_site_detail_view(request, pk):
    project_site = ProjectSite.objects.filter(pk=pk).first()
    context = {'project_site': project_site}
    return render(request, 'project_site/project_site_detail_view.html', context=context)

def customer_project_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        accounts = CustomerProject.objects.filter(cp_name__icontains=query)[:10]
        suggestions = [{'account_id': account.id, 'account_name': account.cp_name} for account in accounts]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})

# @login_required
def project_site_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)
        form = ProjectSiteForm(request.POST)
        if form.is_valid():
            account_name = form.cleaned_data.get('ps_name')

            if ProjectSite.objects.filter(ps_name=account_name).exists():
                form.add_error('ps_name', 'This account already exists.')
            else:
                project_site = form.save(commit=False)
                project_site.ps_project_id = form.cleaned_data.get('ps_project_uuid')
                project_site.save()
                messages.success(request, 'Project site created successfully.')
                return redirect('project_site:project_site_list_view')
        else:
            print(form.errors)
    else:
        form = ProjectSiteForm()
    return render(request, 'project_site/project_site_creation_form.html', {'form': form})

# @login_required
def project_site_edit_form(request, pk):
    if pk:
        account = get_object_or_404(ProjectSite, pk=pk)
    else:
        account = None

    if request.method == 'POST':
        form = ProjectSiteForm(request.POST, instance=account)
        print("All POST data:", request.POST)

        if form.is_valid():
            account_name = form.cleaned_data.get('ps_name')
            print(f"Account name: {account_name}")

            selected_account_id_for_project = form.cleaned_data.get('ps_project_uuid')
            print(f"Selected account ID for project: {selected_account_id_for_project}")
            
            if ProjectSite.objects.filter(ps_name=account_name).exclude(pk=pk).exists():
                form.add_error('ps_name', 'This Project Site already exists.')
            else:
                account = form.save(commit=False)
                account.ps_project_uuid = selected_account_id_for_project
                # Update the ps_project field with the actual project object
                account.ps_project = CustomerProject.objects.get(id=selected_account_id_for_project)
                account.save()

                if pk:
                    messages.success(request, 'Project Site updated successfully.')
                else:
                    messages.success(request, 'Project Site created successfully.')
                
                return redirect('project_site:project_site_list_view')
        else:
            print(form.errors)
    else:
        if account:
            # Ensure that the UUID is correctly set when editing the form
            ps_project_uuid = CustomerProject.objects.filter(cp_name=account.ps_project).values_list('pk', flat=True).first()
            account.ps_project_uuid = ps_project_uuid
            form = ProjectSiteForm(instance=account)
        else:
            form = ProjectSiteForm()

    return render(request, 'project_site/project_site_edit_form.html', {'form': form, 'account': account})
