from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
import pandas as pd


from .models import CustomerAccount, VendorAccount
from .forms import CustomerAccountForm, UploadFileForm, VendorAccountForm


# Create your views here.

from django.http import JsonResponse
from .models import Country, Region



def customer_accounts_list_view(request):
    customer_accounts = list(CustomerAccount.objects.all())
    vendor_accounts = list(VendorAccount.objects.all())

    accounts = customer_accounts + vendor_accounts

    accounts = sorted(customer_accounts + vendor_accounts, key=lambda x: x.updated_at, reverse=True)

    context = {'accounts': accounts}
    return render(request, 'accounts/customer_accounts_list_view.html', context=context)

@require_POST
def select_account_type(request):
    account_type = request.POST.get('account_type')
    if account_type in ['customer', 'vendor']:
        if account_type == 'customer':
            return redirect('accounts:customer_account_creation_form')
        elif account_type == 'vendor':
            return redirect('accounts:vendor_account_creation_form')
    else:
        return render(request, 'select_account_type.html', {'error': 'Invalid account type selection'})



def customer_account_creation_form(request):
    if request.method == 'POST':
        form = CustomerAccountForm(request.POST)
        if form.is_valid():
            account_name = form.cleaned_data.get('ca_name')
            if CustomerAccount.objects.filter(ca_name=account_name).exists():
                form.add_error('ca_name', 'This account already exists.')
            else:
                # account_name = request.POST.get('ca_name')
                # print(account_name)
                # record_type = request.POST.get('ca_record_type')
                # print(record_type)
                # phone_number = request.POST.get('ca_phone_number')
                # print(phone_number)
                # account_owner = request.POST.get('ca_account_owner')
                # print(account_owner)

                # account_type = request.POST.get('ca_type')
                # print(account_type)
                # customer_code = request.POST.get('ca_customer_code')
                # print(customer_code)
                # account_industray = request.POST.get('ca_industray')
                # print(account_industray)
                # account_description = request.POST.get('ca_description')
                # print(account_description)
                # account_payment_terms = request.POST.get('ca_payment_terms')
                # print(account_payment_terms)

                # billing_address = request.POST.get('ca_billing_address')
                # print(billing_address)
                # billing_country = request.POST.get('ca_billing_country')
                # print(billing_country)
                # billing_street = request.POST.get('ca_billing_street')
                # print(billing_street)
                # billing_city = request.POST.get('ca_billing_city')
                # print(billing_city)
                # billing_state = request.POST.get('ca_billing_state')
                # print(billing_state)
                # billing_pin_code = request.POST.get('ca_billing_pin_code')
                # print(billing_pin_code)

                # shipping_address = request.POST.get('ca_shipping_address')
                # print(shipping_address)
                # shipping_country = request.POST.get('ca_shipping_country')
                # print(shipping_country)
                # shipping_street = request.POST.get('ca_shipping_street')
                # print(shipping_street)
                # shipping_city = request.POST.get('ca_shipping_city')
                # print(shipping_city)
                # shipping_state = request.POST.get('ca_shipping_state')
                # print(shipping_state)
                # shipping_pin_code = request.POST.get('ca_shipping_pin_code')
                # print(shipping_pin_code)

                new_account = form.save()
                messages.success(request, 'Customer account created successfully.')
                return redirect('accounts:customer_account_detail_view', pk=new_account.pk)
        else:
            print(form.errors)
    else:
        form = CustomerAccountForm()
    return render(request, 'accounts/customer_account_creation_form.html', {'form': form})


def vendor_account_creation_form(request):
    if request.method == 'POST':
        form = VendorAccountForm(request.POST)
        if form.is_valid():
            account_name = form.cleaned_data.get('va_name')
            if VendorAccount.objects.filter(va_name=account_name).exists():
                form.add_error('va_name', 'This account already exists.')
            else:
                new_account = form.save()
                print(f"New account created : {new_account}")
                messages.success(request, 'Customer account created successfully.')
                return redirect('accounts:vendor_account_detail_view', pk=new_account.pk)
                
        else:
            print(form.errors)
    else:
        form = VendorAccountForm()
    return render(request, 'accounts/vendor_account_creation_form.html', {'form': form})

def get_states_by_country(request):
    country_id = request.GET.get('country_id')
    states = Region.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def customer_account_detail_view(request, pk):
    customer_account = CustomerAccount.objects.filter(pk=pk).first()
    context = {'customer_account': customer_account}
    return render(request, 'accounts/customer_account_detail_view.html', context=context)

def vendor_account_detail_view(request, pk):
    vendor_account = VendorAccount.objects.filter(pk=pk).first()
    context = {'vendor_account': vendor_account}
    return render(request, 'accounts/vendor_account_detail_view.html', context=context)


def customer_account_edit_form(request, pk=None):
    # Retrieve the existing account if editing
    if pk:
        account = get_object_or_404(CustomerAccount, pk=pk)
    else:
        account = None

    if request.method == 'POST':
        form = CustomerAccountForm(request.POST, instance=account)
        if form.is_valid():
            account_name = form.cleaned_data.get('ca_name')
            # Check if account name already exists
            if CustomerAccount.objects.filter(ca_name=account_name).exclude(pk=pk).exists():
                form.add_error('ca_name', 'This account name already exists.')
            else:
                account = form.save()
                if pk:
                    messages.success(request, 'Customer account updated successfully.')
                else:
                    messages.success(request, 'Customer account created successfully.')
                return redirect('accounts:customer_account_detail_view', pk=account.pk)
        # If form is not valid, handle error display
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = CustomerAccountForm(instance=account)

    # Render the form with the current data and errors if any
    return render(request, 'accounts/customer_account_edit_form.html', {'form': form, 'account': account})


def vendor_account_edit_form(request, pk=None):
    # Retrieve the existing account if editing
    if pk:
        account = get_object_or_404(VendorAccount, pk=pk)
    else:
        account = None

    if request.method == 'POST':
        form = VendorAccountForm(request.POST, instance=account)
        if form.is_valid():
            account_name = form.cleaned_data.get('va_name')
            # Check if account name already exists
            if VendorAccount.objects.filter(va_name=account_name).exclude(pk=pk).exists():
                form.add_error('ca_name', 'This account name already exists.')
            else:
                account = form.save()
                if pk:
                    messages.success(request, 'Customer account updated successfully.')
                else:
                    messages.success(request, 'Customer account created successfully.')
                return redirect('accounts:vendor_account_detail_view', pk=account.pk)
        # If form is not valid, handle error display
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = VendorAccountForm(instance=account)

    # Render the form with the current data and errors if any
    return render(request, 'accounts/vendor_account_edit_form.html', {'form': form, 'account': account})



def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            df = pd.read_excel(file, engine='openpyxl')
            
            for index, row in df.iterrows():
                ca_billing_country = None
                ca_billing_state = None
                ca_shipping_country = None
                ca_shipping_state = None

                # Get the billing country if it exists
                if not pd.isna(row['CaBillingCountry']):
                    try:
                        ca_billing_country = Country.objects.get(name=row['CaBillingCountry'])
                    except Country.DoesNotExist:
                        ca_billing_country = None  # or handle this case as needed

                # Get the billing state if it exists
                if not pd.isna(row['CaBillingState']):
                    try:
                        ca_billing_state = Region.objects.get(name=row['CaBillingState'])
                    except Region.DoesNotExist:
                        ca_billing_state = None  # or handle this case as needed

                # Get the shipping country if it exists
                if not pd.isna(row['CaShippingCountry']):
                    try:
                        ca_shipping_country = Country.objects.get(name=row['CaShippingCountry'])
                    except Country.DoesNotExist:
                        ca_shipping_country = None  # or handle this case as needed

                # Get the shipping state if it exists
                if not pd.isna(row['CaShippingState']):
                    try:
                        ca_shipping_state = Region.objects.get(name=row['CaShippingState'])
                    except Region.DoesNotExist:
                        ca_shipping_state = None  # or handle this case as needed

                CustomerAccount.objects.create(
                    ca_name=row['CaName'],
                    record_type=row['CaRecordType'],
                    ca_phone_number=row['CaPhone'] if not pd.isna(row['CaPhone']) else '',
                    ca_account_owner=row['CaAccountOwner'] if not pd.isna(row['CaAccountOwner']) else '',

                    ca_type=row['CaType'],
                    ca_customer_code=row['CaCustomerCode'] if not pd.isna(row['CaCustomerCode']) else '',
                    ca_industray=row['CaIndustry'] if not pd.isna(row['CaIndustry']) else '',
                    ca_description=row['CaDescription'] if not pd.isna(row['CaDescription']) else '',
                    ca_payment_terms=row['CaPaymentTerms'] if not pd.isna(row['CaPaymentTerms']) else '',

                    ca_billing_address=row['CaBillingAddress'] if not pd.isna(row['CaBillingAddress']) else '',
                    ca_billing_country=ca_billing_country,
                    ca_billing_street=row['CaBillingStreet'] if not pd.isna(row['CaBillingStreet']) else '',
                    ca_billing_city=row['CaBillingCity'] if not pd.isna(row['CaBillingCity']) else '',
                    ca_billing_state=ca_billing_state,
                    ca_billing_pin_code=row['CaBillingPostalCode'] if not pd.isna(row['CaBillingPostalCode']) else '',

                    ca_shipping_address=row['CaShippingAddress'] if not pd.isna(row['CaShippingAddress']) else '',
                    ca_shipping_country=ca_shipping_country,
                    ca_shipping_street=row['CaShippingStreet'] if not pd.isna(row['CaShippingStreet']) else '',
                    ca_shipping_city=row['CaShippingCity'] if not pd.isna(row['CaShippingCity']) else '',
                    ca_shipping_state=ca_shipping_state,
                    ca_shipping_pin_code=row['CaShippingPostalCode'] if not pd.isna(row['CaShippingPostalCode']) else '',
                )
            return redirect('accounts:customer_accounts_list_view')  # Replace with your success URL or view
    else:
        form = UploadFileForm()
    return render(request, 'accounts/customer_account_data_upload_form.html', {'form': form})
