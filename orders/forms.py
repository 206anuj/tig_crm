from django import forms
from .models import SalesOrder
from accounts.models import CustomerAccount
from projects.models import CustomerProject

class SalesOrderForm(forms.ModelForm):
    so_record_type = forms.CharField(max_length=100, required=True)
    so_customer_vendor_uuid = forms.CharField(widget=forms.HiddenInput(), required=False) 
    so_project_uuid = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = SalesOrder
        fields = [
                    'so_po_number',
                    'so_po_status',
                    'so_customer_vendor_uuid',
                    'so_project_uuid',
                    'so_comment',
                    'so_tig_entity',
                    'so_po_start_date',
                    'so_po_end_date',
                    'so_currency',
                    'so_po_amount',
                    'so_po_amount_utilised',
                    'so_po_balance',
                    'so_tax_included',
                    'so_bill_to_address',
                    'so_ship_to_address',
                    'so_record_type'
                ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_so_customer_vendor(self):
        # Validate and return cp_customer_vendor as a UUID
        so_customer_vendor_uuid = self.cleaned_data.get('so_customer_vendor_uuid')
        if not so_customer_vendor_uuid:
            raise forms.ValidationError('This field is required.')
        return so_customer_vendor_uuid
    
    def clean_so_project(self):
        # Validate and return cp_end_customer as a UUID
        so_project_uuid = self.cleaned_data.get('so_project_uuid')
        if not so_project_uuid:
            raise forms.ValidationError('This field is required.')
        return so_project_uuid




