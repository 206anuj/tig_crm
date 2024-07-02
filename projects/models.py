from django.db import models
import uuid

from accounts.models import CustomerAccount

# Create your models here.


class CustomerProject(models.Model):

    CUSTOMER_PROJECT_TIG_ENTITY_CHOICES = [
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


    CUSTOMER_PROJECT_PAYMENT_TERM_CHOICES = [
        ('NET0','NET0'),
        ('NET10','NET10'),
        ('NET30','NET30'),
        ('NET45','NET45'),
        ('NET60','NET60'),
        ('NET90','NET90'),
    ]

    CUSTOMER_PROJECT_STATUS_CHOICES = [
        ('Transition','Transition'),
        ('BAU','BAU'),
        ('Descoped','Descoped'),
    ]

    CUSTOMER_PROJECT_REGION_CHOICES = [
        ('APAC','APAC'),
        ('EMEA','EMEA'),
        ('MEA','MEA'),
        ('NA','NA'),
        ('LATAM','LATAM'),
        ('AMEA','AMEA'),
        ('ANZ','ANZ'),
    ]

    CUSTOMER_PROJECT_TYPE_CHOICES = [
        ('Workspace infrastructure','Workspace infrastructure'),
        ('Enterprise Infrastructure','Enterprise Infrastructure'),
    ]

    CUSTOMER_PROJECT_BILLING_FREQUENCY_CHOICES = [
        ('One Time','One Time'),
        ('Weekly','Weekly'),
        ('Bi-Weekly','Bi-Weekly'),
        ('Monthly','Monthly'),
        ('Quarterly','Quarterly'),
        ('Half-Yearly','Half-Yearly'),
        ('Yearly','Yearly'),
        ('ADHOC','ADHOC'),
    ]

    CUSTOMER_PROJECT_CANCELLED_TICKET_BILLABLE_CHOICES = [
        ('Yes','Yes'),
        ('No','No'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Customer Project Information
    cp_name = models.CharField(max_length=255)
    cp_customer_vendor = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, related_name='cp_customer_vendor')
    cp_start_date = models.DateField()
    cp_end_date = models.DateField()
    cp_tig_entity = models.CharField(max_length=64, choices=CUSTOMER_PROJECT_TIG_ENTITY_CHOICES)
    cp_region = models.CharField(max_length=5, choices=CUSTOMER_PROJECT_REGION_CHOICES, blank=True)
    cp_status = models.CharField(max_length=16, choices=CUSTOMER_PROJECT_STATUS_CHOICES, blank=True)
    cp_end_customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, related_name='cp_end_customer')
    cp_type = models.CharField(max_length=32, choices=CUSTOMER_PROJECT_TYPE_CHOICES, blank=True)

    # Customer Project Billing Information
    cp_payment_terms = models.CharField(max_length=8, choices=CUSTOMER_PROJECT_PAYMENT_TERM_CHOICES)
    cp_cancelled_ticket_billable = models.CharField(max_length=4, choices=CUSTOMER_PROJECT_CANCELLED_TICKET_BILLABLE_CHOICES, blank=True)
    cp_cancelled_ticket_mutiplier_1 = models.CharField(max_length=255, blank=True)
    cp_billing_frequency = models.CharField(max_length=16, choices=CUSTOMER_PROJECT_BILLING_FREQUENCY_CHOICES)
    cp_cancellation_window_1 = models.CharField(max_length=255, blank=True)
    cp_cancellation_window_2 = models.CharField(max_length=255, blank=True)
    cp_cancelled_ticket_mutiplier_2 = models.CharField(max_length=255, blank=True)

    # Customer Project Terms & Conditions
    cp_terms_and_conditions = models.TextField(max_length=255, blank=True)

    # Customer Project System Information
    cp_owner = models.CharField(max_length=255, blank=True)
    cp_last_billing_date = models.DateField(blank=True, null=True)
    cp_record_type = models.CharField(max_length=255)

    # Model information 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

    def __str__(self):
        return self.cp_name
