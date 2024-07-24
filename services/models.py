from django.db import models
import uuid
from multiselectfield import MultiSelectField

from projects.models import CustomerProject, VendorProject
from accounts.models import VendorAccount
from project_site.models import ProjectSite
from orders.models import SalesOrder
# Create your models here.

class FteSerivce(models.Model):
 
    FTE_SERVICE_TYPE = [
        ('FTE','FTE'),
   
        ]
 
    FTE_SERVICE_SOURCED_BY = [
        ('TotalIT','TotalIT'),
        ('Vendor','Vendor'),
        
    ]

    FTE_SERVICE_SUBTYPE = [
        ('FTE Overtime Hourly','FTE Overtime Hourly'),
        ('FTE Overtime Half Day','FTE Overtime Half Day'),
        ('FTE Overtime Full Day','FTE Overtime Full Day'),
        ('Backfill Half Day - First Half','Backfill Half Day - First Half'),
        ('Backfill Half Day - Second Half','Backfill Half Day - Second Half'),
        ('Backfill Full Day ','Backfill Full Day'),
        ('Backfill Overtime Hourly','Backfill Overtime Hourly'),
        ('Backfill Overtime Half Day','Backfill Overtime Half Day'),
        ('Backfill Overtime Full Day','Backfill Overtime Full Day'),

    ]

    FTE_SERVICE_CATEGORY = [
        ('EUC(End User Computing)','EUC(End User Computing)'),
        ('Network','Network'),
        ('Server','Server'),
        ('Storage','Storage'),

    ]

    FTE_SERVICE_SKILL_LEVEL = [
        ('L0', 'L0'),
        ('L0.5', 'L0.5'),
        ('L1', 'L1'),
        ('L1.5', 'L1.5'),
        ('L2', 'L2'),
        ('L3', 'L3'),
    ]

    FTE_SERVICE_CUSTOMER_CURRENCY = [
        ('AED - UAE Dirham', 'AED - UAE Dirham'),
        ('AUD - Australian Dollar', 'AUD - Australian Dollar'),
        ('CAD - Canadian Dollar', 'CAD - Canadian Dollar'),
        ('CHF - Swiss Franc', 'CHF - Swiss Franc'),
        ('DKK - Danish Krone', 'DKK - Danish Krone'),
        ('EUR - Euro', 'EUR - Euro'),
        ('GBP - British Pound', 'GBP - British Pound'),
        ('HKD - Hong Kong Dollar', 'HKD - Hong Kong Dollar'),
        ('INR - Indian Rupee', 'INR - Indian Rupee'),
        ('JPY - Japanese Yen', 'JPY - Japanese Yen'),
        ('KRW - Korean Won', 'KRW - Korean Won'),
        ('MYR - Malaysian Ringgit', 'MYR - Malaysian Ringgit'),
        ('NOK - Norwegian Krone', 'NOK - Norwegian Krone'),
        ('NZD - New Zealand Dollar', 'NZD - New Zealand Dollar'),
        ('PLN - Polish Zloty', 'PLN - Polish Zloty'),
        ('SEK - Swedish Krona', 'SEK - Swedish Krona'),
        ('SGD - Singapore Dollar', 'SGD - Singapore Dollar'),
        ('THB - Thai Baht', 'THB - Thai Baht'),
        ('USD - U.S. Dollar', 'USD - U.S. Dollar')

    ]

    FTE_SERVICE_VENDOR_CURRENCY = [
        ('AED - UAE Dirham', 'AED - UAE Dirham'),
        ('AUD - Australian Dollar', 'AUD - Australian Dollar'),
        ('CAD - Canadian Dollar', 'CAD - Canadian Dollar'),
        ('CHF - Swiss Franc', 'CHF - Swiss Franc'),
        ('DKK - Danish Krone', 'DKK - Danish Krone'),
        ('EUR - Euro', 'EUR - Euro'),
        ('GBP - British Pound', 'GBP - British Pound'),
        ('HKD - Hong Kong Dollar', 'HKD - Hong Kong Dollar'),
        ('INR - Indian Rupee', 'INR - Indian Rupee'),
        ('JPY - Japanese Yen', 'JPY - Japanese Yen'),
        ('KRW - Korean Won', 'KRW - Korean Won'),
        ('MYR - Malaysian Ringgit', 'MYR - Malaysian Ringgit'),
        ('NOK - Norwegian Krone', 'NOK - Norwegian Krone'),
        ('NZD - New Zealand Dollar', 'NZD - New Zealand Dollar'),
        ('PLN - Polish Zloty', 'PLN - Polish Zloty'),
        ('SEK - Swedish Krona', 'SEK - Swedish Krona'),
        ('SGD - Singapore Dollar', 'SGD - Singapore Dollar'),
        ('THB - Thai Baht', 'THB - Thai Baht'),
        ('USD - U.S. Dollar', 'USD - U.S. Dollar')

    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    # Information
    fte_serivce_name = models.CharField(max_length=255)
    fte_serivce_project = models.ForeignKey(CustomerProject, on_delete=models.CASCADE, related_name='fte_serivce_project_fk') # this will come from CustomerProject # 
    fte_serivce_project_resource_roaster = models.CharField(max_length=255) # This will come from ProjectResourceRoaster
    fte_serivce_project_site = models.ForeignKey(ProjectSite, on_delete=models.CASCADE, related_name='fte_serivce_project_site_fk') #this will come from Project Site
    fte_serivce_customer_purchase_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='fte_serivce_customer_purchase_order_fk') #this will come from CustomerPurchaseOrder
    fte_serivce_service_type = models.CharField(max_length=255, choices=FTE_SERVICE_TYPE, blank=True) 
    fte_serivce_sourced_by = models.CharField(max_length=255, choices=FTE_SERVICE_SOURCED_BY)
    fte_serivce_subtype_type = MultiSelectField(choices=FTE_SERVICE_SUBTYPE, max_choices=10, max_length=1024, blank=True) # This will be mutiple select field.

 
    # Service Information
    fte_serivce_start_date = models.DateField() # Date
    fte_serivce_end_date = models.DateField() # Date
    fte_serivce_category = MultiSelectField(choices=FTE_SERVICE_CATEGORY, max_choices=10, max_length=1024, blank=True) # This will be mutiple select field.
    # fte_serivce_category = models.CharField(max_length=255, choices=FTE_SERVICE_CATEGORY)
    fte_serivce_skill_level = models.CharField(max_length=255, choices=FTE_SERVICE_SKILL_LEVEL)
    fte_serivce_description = models.TextField(max_length=1024, blank=True)

    # Customer Pricing Details
    fte_serivce_customer_currency = models.CharField(max_length=255, choices=FTE_SERVICE_CUSTOMER_CURRENCY)
    fte_serivce_customer_standby_fees = models.FloatField(null=True, blank=True, default=None) 
    fte_serivce_customer_day_rate = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_additional_hrs_rate_oh = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_monthly_rate = models.FloatField() # This field required
    fte_serivce_customer_additional_hrs_rate_ooh = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_weekend_hourly = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_weekend_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_ot_rate = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_weekend_full_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_ph_hourly = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_tm_rate_hrs = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_ph_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_customer_ph_full_day = models.FloatField(null=True, blank=True, default=None)
 
    # Customer Pricing Details  (PO Currency)
    fte_serivce_customer_quote_po_conversion_rate = models.FloatField(null=True, blank=True, default=None) # this should be a float field
    
    # Vendor Details
    fte_serivce_vendor_name = models.ForeignKey(VendorAccount, on_delete=models.CASCADE, related_name='fte_serivce_vendor_name_fk', null=True, blank=True) #this will come from VendorAccount
    fte_serivce_vendor_project = models.ForeignKey(VendorProject, on_delete=models.CASCADE, related_name='fte_serivce_vendor_project_fk', null=True, blank=True) #this will come from VendorProject
    fte_serivce_purchase_order = models.CharField(max_length=255, blank=True) #this will come from VendorPurchaseOrder
    fte_serivce_vendor_currency = models.CharField(max_length=255, choices=FTE_SERVICE_VENDOR_CURRENCY, blank=True, null=True)
 
    # Vendor Pricing Details
    fte_serivce_vendor_standby_fees = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_day_rate = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_additional_hrs_rate_oh = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_monthly_rate = models.FloatField(null=True, default=None) 
    fte_serivce_vendor_additional_hrs_rate_ooh = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_weekend_hourly = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_weekend_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_ot_rate = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_weekend_full_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_ph_hourly = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_tm_rate_hrs = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_ph_half_day = models.FloatField(null=True, blank=True, default=None)
    fte_serivce_vendor_ph_full_day = models.FloatField(null=True, blank=True, default=None)
 
    # Model information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

    def __str__(self):
        return self.fte_serivce_name
 