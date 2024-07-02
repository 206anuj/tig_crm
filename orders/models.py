from django.db import models
import uuid
from decimal import Decimal

from accounts.models import CustomerAccount
from projects.models import CustomerProject
# Create your models here.

class SalesOrder(models.Model):

    SALES_ORDER_PO_STATUS_CHOICES = [
        ('Released', 'Released'),
        ('Draft', 'Draft'),
    ]

    SALES_ORDER_TIG_ENTITY_CHOICES = [
        ('Total IT Consult LLP','Total IT Consult LLP'),
        ('Total IT Consult Pty ltd','Total IT Consult Pty ltd'),
        ('Total IT Global Pte Ltd','Total IT Global Pte Ltd'),
        ('Total IT Global Sdn. Bhd.','Total IT Global Sdn. Bhd.'),
        ('Total IT Global KK,Japan','Total IT Global KK,Japan'),
        ('TIC Netherlands B.V.','TIC Netherlands B.V.'),
        ('Total IT Global Inc.','Total IT Global Inc.'),
        ('Total IT Global NZ Ltd','Total IT Global NZ Ltd'),
        ('Total IT Global HK Ltd','Total IT Global HK Ltd'),
        ('Total IT Consult DK ApS','Total IT Consult DK ApS'),
        ('Total IT Global Finalnd OY','Total IT Global Finalnd OY'),
        ('TOTAL IT GLOBAL POLAND Sp. z o .o','TOTAL IT GLOBAL POLAND Sp. z o .o'),
        ('Total IT Global France','Total IT Global France'),
        ('Total IT Global Company Limited','Total IT Global Company Limited'),
        ('Total IT Global Germany GMBH','Total IT Global Germany GMBH'),
        ('Total IT Norway AS','Total IT Norway AS'),
        ('TI Global Sweden AB','TI Global Sweden AB'),
        ('Total IT Global UK Limited','Total IT Global UK Limited'),
    ]

    SALES_ORDER_CURRENCY_CHOICES = [
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

    SALAES_ORDER_TAX_INCLUDED_CHOICES = [
        ('Yes','Yes'),
        ('No','No'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Information fields for sales orders
    so_po_number = models.CharField(max_length=32)
    so_po_status = models.CharField(max_length=16, choices=SALES_ORDER_PO_STATUS_CHOICES)
    so_customer_vendor = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, related_name='so_customer_vendor')
    so_project = models.ForeignKey(CustomerProject, on_delete=models.CASCADE, related_name='so_project')
    so_comment = models.TextField(blank=True, max_length=1024)
    so_tig_entity = models.CharField(max_length=64, choices=SALES_ORDER_TIG_ENTITY_CHOICES)

    # PO Details Information fields for sales orders
    so_po_start_date = models.DateField()
    so_po_end_date = models.DateField()
    so_currency = models.CharField(max_length=32, choices=SALES_ORDER_CURRENCY_CHOICES)
    so_po_amount = models.CharField(max_length=10)
    so_po_amount_utilised = models.CharField(max_length=10)
    so_po_balance = models.CharField(max_length=10)
    so_tax_included = models.CharField(max_length=3, choices=SALAES_ORDER_TAX_INCLUDED_CHOICES)

    # Address Information fields for sales orders
    so_bill_to_address = models.TextField(max_length=1024)
    so_ship_to_address = models.TextField(max_length=1024)

    # System Information fields for sales orders
    so_record_type = models.CharField(max_length=32)

    # Model information 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

    def __str__(self):
        return self.so_po_number

