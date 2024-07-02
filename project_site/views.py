from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ProjectSite
from .forms import ProjectSiteForm
# Create your views here.

def project_site_list_view(request):
    project_sites = ProjectSite.objects.all()
    context = {'project_sites': project_sites}
    return render(request, 'project_site/project_site_list_view.html', context=context)

def project_site_detail_view(request, pk):
    project_site = ProjectSite.objects.filter(pk=pk).first()
    context = {'project_site': project_site}
    return render(request, 'project_site/project_site_detail_view.html', context=context)

def project_site_creation_form(request):
    if request.method == 'POST':
        all_post_data = request.POST
        print("All POST data:", all_post_data)

        form = ProjectSiteForm(request.POST)
        print(f"This is {request.POST.get('ps_name')}")
        
        if form.is_valid():
            project_site = form.cleaned_data.get('ps_name')
            print(f"project site name: {project_site}")

            # selected_account_id_for_customer_vendor = request.POST.get('cp_customer_vendor_uuid', None)
            # selected_account_id_for_end_customer = request.POST.get('cp_end_customer_uuid', None)

            # print(f"selected_account_id_for_customer_vendor {selected_account_id_for_customer_vendor}")
            
            if ProjectSite.objects.filter(ps_name=project_site).exists():
                form.add_error('ps_name', 'This Project Site already exists.')
            
            else:
                form.save()
                # new_account = form.save(commit=False)
                # new_account.cp_customer_vendor_id = selected_account_id_for_customer_vendor
                # new_account.cp_end_customer_id = selected_account_id_for_end_customer
                # new_account.save()
                messages.success(request, 'Customer project created successfully.')
                return redirect('project_site:project_site_list_view')
                # return redirect('projects:customer_project_detail_view', pk=new_account.pk)
        
        else:
            print(form.errors)
    
    else:
        form = ProjectSiteForm()
    # return render(request, 'projects/test.html', {'form': form})
    return render(request, 'project_site/project_site_creation_form.html', {'form': form})
