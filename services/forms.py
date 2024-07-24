from django import forms
from .models import FteSerivce
from projects.models import CustomerProject, VendorProject
from accounts.models import VendorAccount
from project_site.models import ProjectSite
from orders.models import SalesOrder

class FteServiceForm(forms.ModelForm):
    fte_serivce_project_uuid = forms.CharField(widget=forms.HiddenInput(), required=True)
    fte_serivce_project_site_uuid = forms.CharField(widget=forms.HiddenInput(), required=True)
    fte_serivce_customer_purchase_order_uuid = forms.CharField(widget=forms.HiddenInput(), required=True)
    fte_serivce_vendor_name_uuid = forms.CharField(widget=forms.HiddenInput(), required=False)
    fte_serivce_vendor_project_uuid = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = FteSerivce
        fields = [
            'fte_serivce_name',
            'fte_serivce_project_uuid',
            'fte_serivce_project_resource_roaster',
            'fte_serivce_project_site_uuid',
            'fte_serivce_customer_purchase_order_uuid',
            'fte_serivce_service_type',
            'fte_serivce_sourced_by',
            'fte_serivce_subtype_type',
            'fte_serivce_start_date',
            'fte_serivce_end_date',
            'fte_serivce_category',
            'fte_serivce_skill_level',
            'fte_serivce_description',
            'fte_serivce_customer_currency',
            'fte_serivce_customer_standby_fees',
            'fte_serivce_customer_day_rate',
            'fte_serivce_customer_additional_hrs_rate_oh',
            'fte_serivce_customer_monthly_rate',
            'fte_serivce_customer_additional_hrs_rate_ooh',
            'fte_serivce_customer_weekend_hourly',
            'fte_serivce_customer_half_day',
            'fte_serivce_customer_weekend_half_day',
            'fte_serivce_customer_ot_rate',
            'fte_serivce_customer_weekend_full_day',
            'fte_serivce_customer_ph_hourly',
            'fte_serivce_customer_tm_rate_hrs',
            'fte_serivce_customer_ph_half_day',
            'fte_serivce_customer_ph_full_day',
            'fte_serivce_customer_quote_po_conversion_rate',
            'fte_serivce_vendor_name_uuid',
            'fte_serivce_vendor_project_uuid',
            'fte_serivce_purchase_order',
            'fte_serivce_vendor_currency',
            'fte_serivce_vendor_standby_fees',
            'fte_serivce_vendor_day_rate',
            'fte_serivce_vendor_additional_hrs_rate_oh',
            'fte_serivce_vendor_monthly_rate',
            'fte_serivce_vendor_additional_hrs_rate_ooh',
            'fte_serivce_vendor_weekend_hourly',
            'fte_serivce_vendor_half_day',
            'fte_serivce_vendor_weekend_half_day',
            'fte_serivce_vendor_ot_rate',
            'fte_serivce_vendor_weekend_full_day',
            'fte_serivce_vendor_ph_hourly',
            'fte_serivce_vendor_tm_rate_hrs',
            'fte_serivce_vendor_ph_half_day',
            'fte_serivce_vendor_ph_full_day',
        ]

    def clean_fte_serivce_project_uuid(self):
        fte_serivce_project_uuid = self.cleaned_data.get('fte_serivce_project_uuid')
        if not fte_serivce_project_uuid:
            raise forms.ValidationError('This field is required.')
        if not CustomerProject.objects.filter(id=fte_serivce_project_uuid).exists():
            raise forms.ValidationError('Invalid customer project selected.')
        return fte_serivce_project_uuid

    def clean_fte_serivce_project_site_uuid(self):
        fte_serivce_project_site_uuid = self.cleaned_data.get('fte_serivce_project_site_uuid')
        if not fte_serivce_project_site_uuid:
            raise forms.ValidationError('This field is required.')
        if not ProjectSite.objects.filter(id=fte_serivce_project_site_uuid).exists():
            raise forms.ValidationError('Invalid project site selected.')
        return fte_serivce_project_site_uuid

    def clean_fte_serivce_customer_purchase_order_uuid(self):
        fte_serivce_customer_purchase_order_uuid = self.cleaned_data.get('fte_serivce_customer_purchase_order_uuid')
        if not fte_serivce_customer_purchase_order_uuid:
            raise forms.ValidationError('This field is required.')
        if not SalesOrder.objects.filter(id=fte_serivce_customer_purchase_order_uuid).exists():
            raise forms.ValidationError('Invalid sales order selected.')
        return fte_serivce_customer_purchase_order_uuid

    def clean_fte_serivce_vendor_name_uuid(self):
        fte_serivce_vendor_name_uuid = self.cleaned_data.get('fte_serivce_vendor_name_uuid')
        if fte_serivce_vendor_name_uuid and not VendorAccount.objects.filter(id=fte_serivce_vendor_name_uuid).exists():
            raise forms.ValidationError('Invalid vendor name selected.')
        return fte_serivce_vendor_name_uuid

    def clean_fte_serivce_vendor_project_uuid(self):
        fte_serivce_vendor_project_uuid = self.cleaned_data.get('fte_serivce_vendor_project_uuid')
        if fte_serivce_vendor_project_uuid and not VendorProject.objects.filter(id=fte_serivce_vendor_project_uuid).exists():
            raise forms.ValidationError('Invalid vendor project selected.')
        return fte_serivce_vendor_project_uuid

    def clean(self):
        cleaned_data = super().clean()
        service_start_date = cleaned_data.get('fte_serivce_start_date')
        service_end_date = cleaned_data.get('fte_serivce_end_date')
        sales_order_uuid = cleaned_data.get('fte_serivce_customer_purchase_order_uuid')
        customer_currency = cleaned_data.get('fte_serivce_customer_currency')
        conversion_rate = cleaned_data.get('fte_serivce_customer_quote_po_conversion_rate')

        if sales_order_uuid:
            try:
                sales_order = SalesOrder.objects.get(id=sales_order_uuid)
                po_start_date = sales_order.so_po_start_date
                po_end_date = sales_order.so_po_end_date

                if not (po_start_date <= service_start_date <= po_end_date):
                    self.add_error('fte_serivce_start_date', "Service start date must be within the PO start and end dates.")
                if not (po_start_date <= service_end_date <= po_end_date):
                    self.add_error('fte_serivce_end_date', "Service end date must be within the PO start and end dates.")
                if service_start_date > service_end_date:
                    self.add_error('fte_serivce_start_date', "Service start date must be before the service end date.")

                # Check currency and conversion rate requirement
                if sales_order.so_currency != customer_currency and not conversion_rate:
                    self.add_error('fte_serivce_customer_quote_po_conversion_rate', "Conversion rate is required if the customer currency differs from the purchase order currency.")

            except SalesOrder.DoesNotExist:
                self.add_error('fte_serivce_customer_purchase_order_uuid', "Sales order does not exist.")

        return cleaned_data
