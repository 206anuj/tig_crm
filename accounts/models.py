from django.db import models
import uuid
from django.contrib.auth.models import User
from cities_light.models import Country, Region

# Create your models here.

class CustomerAccount(models.Model):

    CUSTOMER_ACCOUNT_TYPE_CHOICES = [
        ('Prospect','Prospect'),
        ('Customer Direct','Customer Direct'),
        ('Customer Channel','Customer Channel'),
        ('Channel','Channel'),
        ('Partner / Reseller','Partner / Reseller'),
        ('Installation Partner','Installation Partner'),
        ('Technology Partner','Technology Partner'),
        ('Other','Other'),
    ]

    CUSTOMER_ACCOUNT_INDUSTRY_CHOICES = [
        ('IT', 'IT'),
        ('Agriculture', 'Agriculture'),
        ('Apparel', 'Apparel'),
        ('Banking', 'Banking'),
        ('Chemicals', 'Chemicals'),
        ('Construction', 'Construction'),
        ('Consulting', 'Consulting'),
        ('Education', 'Education'),
        ('Electronics', 'Electronics'),
        ('Energy', 'Energy'),
        ('Engineering', 'Engineering'),
        ('Finance', 'Finance'),
        ('Government', 'Government'),
        ('Healthcare', 'Healthcare'),
        ('Insurance', 'Insurance'),
        ('Machinery', 'Machinery'),
        ('Media', 'Media'),
        ('Recreation', 'Recreation'),
        ('Retail', 'Retail'),
        ('Shipping', 'Shipping'),
        ('Technology', 'Technology'),
        ('Biotechnology', 'Biotechnology'),
        ('Communications', 'Communications'),
        ('Entertainment', 'Entertainment'),
        ('Environmental', 'Environmental'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Manufacturing', 'Manufacturing'),
        ('Not For Profit', 'Not For Profit'),
        ('Telecommunications', 'Telecommunications'),
        ('Transportation', 'Transportation'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]

    CUSTOMER_ACCOUNT_PAYMENT_TERM_CHOICES = [
        ('NET0','NET0'),
        ('NET10','NET10'),
        ('NET30','NET30'),
        ('NET45','NET45'),
        ('NET60','NET60'),
        ('NET90','NET90'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Account Information
    ca_name = models.CharField(max_length=255)
    ca_record_type = models.CharField(max_length=255)
    ca_phone_number = models.CharField(max_length=11, blank=True)
    ca_account_owner = models.CharField(max_length=255, blank=True)

    # Account Other Info
    ca_type = models.CharField(max_length=64, choices=CUSTOMER_ACCOUNT_TYPE_CHOICES)
    ca_customer_code = models.CharField(max_length=255, blank=True)
    ca_industray = models.CharField(max_length=64, choices=CUSTOMER_ACCOUNT_INDUSTRY_CHOICES, blank=True)
    ca_description = models.TextField(max_length=1024, blank=True)
    ca_payment_terms = models.CharField(max_length=64, choices=CUSTOMER_ACCOUNT_PAYMENT_TERM_CHOICES, blank=True)
    
    #Address Information (Billing Information)
    ca_billing_address = models.CharField(max_length=1024, blank=True)
    ca_billing_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='billing_customer_accounts')
    ca_billing_street = models.TextField(max_length=1024, blank=True)
    ca_billing_city = models.CharField(max_length=255, blank=True)
    ca_billing_state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='billing_customer_accounts')
    ca_billing_pin_code = models.CharField(max_length=64, blank=True)

    # Address Information (shipping Information)
    ca_shipping_address = models.CharField(max_length=1024, blank=True)
    ca_shipping_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='shipping_customer_accounts')
    ca_shipping_street = models.TextField(max_length=1024, blank=True)
    ca_shipping_city = models.CharField(max_length=255, blank=True)
    ca_shipping_state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='shipping_customer_accounts')
    ca_shipping_pin_code = models.CharField(max_length=64, blank=True)

    # Model information 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

    def __str__(self):
        return self.ca_name
    


# class VendorAccount(models.Model):

#     VENDOR_ACCOUNT_STATUS_CHOICES = [
#         ('Draft', 'Draft'),
#         ('NDA Signed', 'NDA Signed'),
#         ('Sent for Approval', 'Sent for Approval'),
#         ('Inactive', 'Inactive'),
#         ('Suspended', 'Suspended'),
#         ('Request for DeActivation', 'Request for DeActivation'),
#         ('DeActivation Pending', 'DeActivation Pending'),
#         ('Initiation', 'Initiation'),
#         ('NDA', 'NDA'),
#         ('VRF', 'VRF'),
#         ('Due Diligence', 'Due Diligence'),
#         ('MSA', 'MSA'),
#         ('Registration', 'Registration'),
#         ('Active', 'Active'),
#         ('Rejected', 'Rejected'),
#         ('Blacklisted', 'Blacklisted'),
#     ]
#     VENDOR_ACCOUNT_TYPE_CHOICES = [
#         ('Prospect','Prospect'),
#         ('Customer Direct','Customer Direct'),
#         ('Customer Channel','Customer Channel'),
#         ('Channel','Channel'),
#         ('Partner / Reseller','Partner / Reseller'),
#         ('Installation Partner','Installation Partner'),
#         ('Technology Partner','Technology Partner'),
#         ('Other','Other'),
#     ]
#     VENDOR_ACCOUNT_PARTNER_TYPE_CHOICES = [
#         ('Contractor', 'Contractor'),
#         ('Service Provider', 'Service Provider'),
#         ('Indirect', 'Indirect'),
#         ('Payroll Engineers', 'Payroll Engineers'),
#     ]
#     VENDOR_ACCOUNT_PARTNER_EXPENSE_TYPE_CHOICES = [
#         ('Direct', 'Direct'),
#         ('Indirect', 'Indirect'),
#         ('Both', 'Both'),
#     ]

#     VENDOR_ACCOUNT_INDUSTRY_CHOICES = [
#         ('IT', 'IT'),
#         ('Agriculture', 'Agriculture'),
#         ('Apparel', 'Apparel'),
#         ('Banking', 'Banking'),
#         ('Chemicals', 'Chemicals'),
#         ('Construction', 'Construction'),
#         ('Consulting', 'Consulting'),
#         ('Education', 'Education'),
#         ('Electronics', 'Electronics'),
#         ('Energy', 'Energy'),
#         ('Engineering', 'Engineering'),
#         ('Finance', 'Finance'),
#         ('Government', 'Government'),
#         ('Healthcare', 'Healthcare'),
#         ('Insurance', 'Insurance'),
#         ('Machinery', 'Machinery'),
#         ('Media', 'Media'),
#         ('Recreation', 'Recreation'),
#         ('Retail', 'Retail'),
#         ('Shipping', 'Shipping'),
#         ('Technology', 'Technology'),
#         ('Biotechnology', 'Biotechnology'),
#         ('Communications', 'Communications'),
#         ('Entertainment', 'Entertainment'),
#         ('Environmental', 'Environmental'),
#         ('Food & Beverage', 'Food & Beverage'),
#         ('Manufacturing', 'Manufacturing'),
#         ('Not For Profit', 'Not For Profit'),
#         ('Telecommunications', 'Telecommunications'),
#         ('Transportation', 'Transportation'),
#         ('Utilities', 'Utilities'),
#         ('Other', 'Other'),
#     ]

#     VENDOR_ACCOUNT_COUNTRY_CODE_CHOICES = [
#         ('AF', 'AF'),
#         ('AL', 'AL'),
#         ('DZ', 'DZ'),
#         ('AS', 'AS'),
#         ('AD', 'AD'),
#         ('AO', 'AO'),
#         ('AI', 'AI'),
#         ('AQ', 'AQ'),
#         ('AG', 'AG'),
#         ('AR', 'AR'),
#         ('AM', 'AM'),
#         ('AW', 'AW'),
#         ('AU', 'AU'),
#         ('AT', 'AT'),
#         ('AZ', 'AZ'),
#         ('BS', 'BS'),
#         ('BH', 'BH'),
#         ('BD', 'BD'),
#         ('BB', 'BB'),
#         ('BY', 'BY'),
#         ('BE', 'BE'),
#         ('BZ', 'BZ'),
#         ('BJ', 'BJ'),
#         ('BM', 'BM'),
#         ('BT', 'BT'),
#         ('BO', 'BO'),
#         ('BA', 'BA'),
#         ('BW', 'BW'),
#         ('BV', 'BV'),
#         ('BR', 'BR'),
#         ('IO', 'IO'),
#         ('BN', 'BN'),
#         ('BG', 'BG'),
#         ('BF', 'BF'),
#         ('BI', 'BI'),
#         ('KH', 'KH'),
#         ('CM', 'CM'),
#         ('CA', 'CA'),
#         ('CV', 'CV'),
#         ('KY', 'KY'),
#         ('CF', 'CF'),
#         ('TD', 'TD'),
#         ('CL', 'CL'),
#         ('CN', 'CN'),
#         ('CX', 'CX'),
#         ('CC', 'CC'),
#         ('CO', 'CO'),
#         ('KM', 'KM'),
#         ('CG', 'CG'),
#         ('CD', 'CD'),
#         ('CK', 'CK'),
#         ('CR', 'CR'),
#         ('CI', 'CI'),
#         ('HR', 'HR'),
#         ('CU', 'CU'),
#         ('CY', 'CY'),
#         ('CZ', 'CZ'),
#         ('DK', 'DK'),
#         ('DJ', 'DJ'),
#         ('DM', 'DM'),
#         ('DO', 'DO'),
#         ('TP', 'TP'),
#         ('EC', 'EC'),
#         ('EG', 'EG'),
#         ('SV', 'SV'),
#         ('GQ', 'GQ'),
#         ('ER', 'ER'),
#         ('EE', 'EE'),
#         ('ET', 'ET'),
#         ('XA', 'XA'),
#         ('FK', 'FK'),
#         ('FO', 'FO'),
#         ('FJ', 'FJ'),
#         ('FI', 'FI'),
#         ('FR', 'FR'),
#         ('GF', 'GF'),
#         ('PF', 'PF'),
#         ('TF', 'TF'),
#         ('GA', 'GA'),
#         ('GM', 'GM'),
#         ('GE', 'GE'),
#         ('DE', 'DE'),
#         ('GH', 'GH'),
#         ('GI', 'GI'),
#         ('GR', 'GR'),
#         ('GL', 'GL'),
#         ('GD', 'GD'),
#         ('GP', 'GP'),
#         ('GU', 'GU'),
#         ('GT', 'GT'),
#         ('XU', 'XU'),
#         ('GN', 'GN'),
#         ('GW', 'GW'),
#         ('GY', 'GY'),
#         ('HT', 'HT'),
#         ('HM', 'HM'),
#         ('HN', 'HN'),
#         ('HK', 'HK'),
#         ('HU', 'HU'),
#         ('IS', 'IS'),
#         ('IN', 'IN'),
#         ('ID', 'ID'),
#         ('IR', 'IR'),
#         ('IQ', 'IQ'),
#         ('IE', 'IE'),
#         ('IL', 'IL'),
#         ('IT', 'IT'),
#         ('JM', 'JM'),
#         ('JP', 'JP'),
#         ('XJ', 'XJ'),
#         ('JO', 'JO'),
#         ('KZ', 'KZ'),
#         ('KE', 'KE'),
#         ('KI', 'KI'),
#         ('KP', 'KP'),
#         ('KR', 'KR'),
#         ('KW', 'KW'),
#         ('KG', 'KG'),
#         ('LA', 'LA'),
#         ('LV', 'LV'),
#         ('LB', 'LB'),
#         ('LS', 'LS'),
#         ('LR', 'LR'),
#         ('LY', 'LY'),
#         ('LI', 'LI'),
#         ('LT', 'LT'),
#         ('LU', 'LU'),
#         ('MO', 'MO'),
#         ('MK', 'MK'),
#         ('MG', 'MG'),
#         ('MW', 'MW'),
#         ('MY', 'MY'),
#         ('MV', 'MV'),
#         ('ML', 'ML'),
#         ('MT', 'MT'),
#         ('XM', 'XM'),
#         ('MH', 'MH'),
#         ('MQ', 'MQ'),
#         ('MR', 'MR'),
#         ('MU', 'MU'),
#         ('YT', 'YT'),
#         ('MX', 'MX'),
#         ('FM', 'FM'),
#         ('MD', 'MD'),
#         ('MC', 'MC'),
#         ('MN', 'MN'),
#         ('MS', 'MS'),
#         ('MA', 'MA'),
#         ('MZ', 'MZ'),
#         ('MM', 'MM'),
#         ('NA', 'NA'),
#         ('NR', 'NR'),
#         ('NP', 'NP'),
#         ('AN', 'AN'),
#         ('NL', 'NL'),
#         ('NC', 'NC'),
#         ('NZ', 'NZ'),
#         ('NI', 'NI'),
#         ('NE', 'NE'),
#         ('NG', 'NG'),
#         ('NU', 'NU'),
#         ('NF', 'NF'),
#         ('MP', 'MP'),
#         ('NO', 'NO'),
#         ('OM', 'OM'),
#         ('PK', 'PK'),
#         ('PW', 'PW'),
#         ('PS', 'PS'),
#         ('PA', 'PA'),
#         ('PG', 'PG'),
#         ('PY', 'PY'),
#         ('PE', 'PE'),
#         ('PH', 'PH'),
#         ('PN', 'PN'),
#         ('PL', 'PL'),
#         ('PT', 'PT'),
#         ('PR', 'PR'),
#         ('QA', 'QA'),
#         ('RE', 'RE'),
#         ('RO', 'RO'),
#         ('RU', 'RU'),
#         ('RW', 'RW'),
#         ('SH', 'SH'),
#         ('KN', 'KN'),
#         ('LC', 'LC'),
#         ('PM', 'PM'),
#         ('VC', 'VC'),
#         ('WS', 'WS'),
#         ('SM', 'SM'),
#         ('ST', 'ST'),
#         ('SA', 'SA'),
#         ('SN', 'SN'),
#         ('RS', 'RS'),
#         ('SC', 'SC'),
#         ('SL', 'SL'),
#         ('SG', 'SG'),
#         ('SK', 'SK'),
#         ('SI', 'SI'),
#         ('XG', 'XG'),
#         ('SB', 'SB'),
#         ('SO', 'SO'),
#         ('ZA', 'ZA'),
#         ('GS', 'GS'),
#         ('SS', 'SS'),
#         ('ES', 'ES'),
#         ('LK', 'LK'),
#         ('SD', 'SD'),
#         ('SR', 'SR'),
#         ('SJ', 'SJ'),
#         ('SZ', 'SZ'),
#         ('SE', 'SE'),
#         ('CH', 'CH'),
#         ('SY', 'SY'),
#         ('TW', 'TW'),
#         ('TJ', 'TJ'),
#         ('TZ', 'TZ'),
#         ('TH', 'TH'),
#         ('TG', 'TG'),
#         ('TK', 'TK'),
#         ('TO', 'TO'),
#         ('TT', 'TT'),
#         ('TN', 'TN'),
#         ('TR', 'TR'),
#         ('TM', 'TM'),
#         ('TC', 'TC'),
#         ('TV', 'TV'),
#         ('UG', 'UG'),
#         ('UA', 'UA'),
#         ('AE', 'AE'),
#         ('GB', 'GB'),
#         ('US', 'US'),
#         ('UM', 'UM'),
#         ('UY', 'UY'),
#         ('UZ', 'UZ'),
#         ('VU', 'VU'),
#         ('VA', 'VA'),
#         ('VE', 'VE'),
#         ('VN', 'VN'),
#         ('VG', 'VG'),
#         ('VI', 'VI'),
#         ('WF', 'WF'),
#         ('EH', 'EH'),
#         ('YE', 'YE'),
#         ('YU', 'YU'),
#         ('ZM', 'ZM'),
#         ('ZW', 'ZW'),
#     ]

#     # Vendor Information  
#     va_account_name = models.CharField(max_length=512)
#     va_phone_number = models.CharField(max_length=11, blank=True)
#     va_record_type = models.CharField(max_length=255)
#     va_company_group = models.CharField(max_length=255)
#     va_account_status = models.CharField(max_length=64, choices=VENDOR_ACCOUNT_STATUS_CHOICES)
#     # Vendor Other Information
#     va_account_type = models.CharField(max_length=64, choices=VENDOR_ACCOUNT_TYPE_CHOICES)
#     va_partner_type = models.CharField(max_length=64, choices=VENDOR_ACCOUNT_PARTNER_TYPE_CHOICES)
#     va_partner_expense_type = models.CharField(max_length=64, choices=VENDOR_ACCOUNT_PARTNER_EXPENSE_TYPE_CHOICES)
#     va_industry = models.CharField(max_length=64, choices=VENDOR_ACCOUNT_INDUSTRY_CHOICES)
#     va_total_amount_spent = models.IntegerField()
#     # Vendor Bank Information
#     va_bank_account_number = models.CharField(max_length=255)
#     va_bank_branch = models.CharField(max_length=255)
#     va_bank_account_holder_name = models.CharField(max_length=255)
#     va_bank_branch_code = models.CharField(max_length=255)
#     va_bank_bank_name = models.CharField(max_length=255)
#     va_bank_branch_address = models.CharField(max_length=255)
#     va_bank_account_country_code = models.CharField(max_length=2, choices=VENDOR_ACCOUNT_COUNTRY_CODE_CHOICES)
#     va_bank_ifsc_code = models.CharField(max_length=255)
#     va_bank_zip_code = models.CharField(max_length=255)
#     va_bank_swift_code = models.CharField(max_length=255)
#     va_bank_bank_id = models.CharField(max_length=255)
#     va_bank_sort_code = models.CharField(max_length=255)
#     va_bank_state = models.CharField(max_length=255)
#     va_bank_bsb_code = models.CharField(max_length=55)
#     va_benen_bank_account_type = models.CharField(max_length=255)
#     va_bank_transit_number = models.CharField(max_length=255)
#     va_bank_tax_id = models.CharField(max_length=255)
#     va_bank_routing_number = models.CharField(max_length=255)
#     va_bank_iban = models.CharField(max_length=255)
#     # Vendor Company Overview
#     va_company_name = models.CharField(max_length=255)
#     va_country_headquartered = models.CharField(max_length=255)
#     va_employees_on_payroll = models.PositiveIntegerField()
#     # Vendor Company Registration Details
#     va_company_registration_number = models.CharField(max_length=255)
#     va_gst_vat_registration_number = models.CharField(max_length=255)
#     va_statutory_details = models.TextField()
#     va_service_tax_registration_number = models.CharField(max_length=100)
#     va_tax_identification_number = models.CharField(max_length=100)
#     va_accept_bank_payments_usd = models.BooleanField(default=False)
#     va_accept_bank_payments_euro = models.BooleanField(default=False)
#     # Vendor Employees & Call Support Activity
#     va_provide_24x7_support = models.BooleanField(default=False)
#     va_multilingual_helpdesk = models.BooleanField(default=False)
#     va_support_calls_per_month = models.PositiveIntegerField(default=0)
#     va_communication_method = models.CharField(max_length=100, blank=True)
#     va_company_web_access_for_calls = models.BooleanField(default=False)
#     va_english_speaking_engineers_for_support = models.PositiveIntegerField(default=0)
#     va_english_speaking_engineers_for_tig = models.PositiveIntegerField(default=0)
#     va_call_logging_process = models.CharField(max_length=255, blank=True)
#     # vendor documentation list
#     va_certificate_of_incorporate = models.FileField(upload_to='documents/', blank=True)
#     va_tax_information = models.TextField(blank=True)
#     va_cancel_check_bank_account_number = models.CharField(max_length=255, blank=True)
#     va_gst_vat_registration_certificate = models.FileField(upload_to='documents/', blank=True)
#     # Due Diligence
#     va_due_diligence_partner = models.CharField(max_length=100, blank=True)
#     va_due_diligence_status = models.CharField(max_length=100, blank=True)
#     #Address Information (Billing Information)
#     va_billing_address = models.CharField(max_length=1024, blank=True)
#     va_billing_country = models.CharField(max_length=2, choices=CUSTOMER_ACCOUNT_COUNTRY_CHOICES, blank=True)
#     va_billing_street = models.TextField(max_length=1024, blank=True)
#     va_billing_city = models.CharField(max_length=255, blank=True)
#     va_billing_state = models.CharField(max_length=64, blank=True)
#     va_billing_pin_code = models.CharField(max_length=64, blank=True)
#     # Address Information (shipping Information)
#     va_shipping_address = models.CharField(max_length=1024, blank=True)
#     va_shipping_country = models.CharField(max_length=2, choices=CUSTOMER_ACCOUNT_COUNTRY_CHOICES, blank=True)
#     va_shipping_street = models.TextField(max_length=1024, blank=True)
#     va_shipping_city = models.CharField(max_length=255, blank=True)
#     va_shipping_state = models.CharField(max_length=64, blank=True)
#     va_shipping_pin_code = models.CharField(max_length=64, blank=True)
    
