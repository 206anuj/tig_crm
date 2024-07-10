from django import forms
from .models import CustomerAccount, VendorAccount

class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        fields = '__all__'
        labels = {
            'ca_name': 'Account Name',
            'ca_record_type': 'Record Type',
            'ca_phone_number': 'Phone Number',
            'ca_account_owner': 'Account Owner',
            'ca_type': 'Account Type',
            'ca_customer_code': 'Customer Code',
            'ca_industray': 'Industry',
            'ca_description': 'Description',
            'ca_payment_terms': 'Payment Terms',
            'ca_billing_address': 'Billing Address',
            'ca_billing_country': 'Billing Country',
            'ca_billing_street': 'Billing Street',
            'ca_billing_city': 'Billing City',
            'ca_billing_state': 'Billing State',
            'ca_billing_pin_code': 'Billing Pin Code',
            'ca_shipping_address': 'Shipping Address',
            'ca_shipping_country': 'Shipping Country',
            'ca_shipping_street': 'Shipping Street',
            'ca_shipping_city': 'Shipping City',
            'ca_shipping_state': 'Shipping State',
            'ca_shipping_pin_code': 'Shipping Pin Code',
        }

        # def clean_ca_name(self):
        #     ca_name = self.cleaned_data.get('ca_name')
        #     pk = self.instance.pk
        #     if CustomerAccount.objects.filter(ca_name=ca_name).exclude(pk=pk).exists():
        #         raise forms.ValidationError('This account already exists.')
        #     return ca_name


class UploadFileForm(forms.Form):
    file = forms.FileField()



class VendorAccountForm(forms.ModelForm):

    class Meta:
        model = VendorAccount
        fields = '__all__'