from django import forms
from .models import CustomerProject, VendorProject
from accounts.models import CustomerAccount
 
class CustomerProjectForm(forms.ModelForm):
    record_type = forms.CharField(max_length=100, required=True)
    cp_customer_vendor_uuid = forms.CharField(widget=forms.HiddenInput())
    cp_end_customer_uuid = forms.CharField(widget=forms.HiddenInput())
   
    class Meta:
        model = CustomerProject
        fields = ['cp_name', 'cp_customer_vendor_uuid', 'cp_start_date', 'cp_tig_entity',
                  'cp_region', 'cp_status', 'cp_end_customer_uuid', 'cp_end_date', 'cp_type',
                  'cp_payment_terms', 'cp_cancelled_ticket_billable', 'cp_cancelled_ticket_mutiplier_1',
                  'cp_billing_frequency', 'cp_cancellation_window_1', 'cp_cancelled_ticket_mutiplier_2',
                  'cp_terms_and_conditions', 'cp_owner', 'cp_last_billing_date', 'record_type']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def clean_cp_customer_vendor(self):
        # Validate and return cp_customer_vendor as a UUID
        cp_customer_vendor_uuid = self.cleaned_data.get('cp_customer_vendor_uuid')
        if not cp_customer_vendor_uuid:
            raise forms.ValidationError('This field is required.')
        return cp_customer_vendor_uuid
   
    def clean_cp_end_customer(self):
        # Validate and return cp_end_customer as a UUID
        cp_end_customer_uuid = self.cleaned_data.get('cp_end_customer_uuid')
        if not cp_end_customer_uuid:
            raise forms.ValidationError('This field is required.')
        return cp_end_customer_uuid
 
 
class VendorProjectForm(forms.ModelForm):
    record_type =forms.CharField(max_length=100, required=True)
    vp_vendor_account_uuid = forms.CharField(widget=forms.HiddenInput())
    vp_customer_project_uuid = forms.CharField(widget=forms.HiddenInput())
 
    class Meta:
        model = VendorProject
        fields = ['vp_name','vp_status','vp_vendor_account_uuid','vp_customer_project_uuid','vp_project_start_date',
                  'vp_project_end_date','vp_tig_entity_name','vp_type_of_project','vp_region','vp_payment_terms',
                  'vp_billing_frequency','vp_terms_and_condition','vp_owner','record_type'
                  ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def clean_cp_customer_vendor(self):
        # Validate and return vp_vendor_account as a UUID
        vp_vendor_account_uuid = self.cleaned_data.get('vp_vendor_account_uuid')
        if not vp_vendor_account_uuid:
            raise forms.ValidationError('This field is required.')
        return vp_vendor_account_uuid
   
    def clean_cp_end_customer(self):
        # Validate and return cp_end_customer as a UUID
        vp_customer_project_uuid = self.cleaned_data.get('vp_customer_project_uuid')
        if not vp_customer_project_uuid:
            raise forms.ValidationError('This field is required.')
        return vp_customer_project_uuid