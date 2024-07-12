from django.db import models
import uuid
 
from accounts.models import CustomerAccount, VendorAccount
 
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
    record_type = models.CharField(max_length=255)
 
    # Model information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')
 
    def __str__(self):
        return self.cp_name
 
 
 
 
 
# vendor project
 
class VendorProject(models.Model):
 
    VENDOR_PROJECT_STATUS_CHOICES =[
        ('Transition','Transition'),
        ('BAU','BAU'),
        ('Hold','Hold'),
        ('Terminated','Terminated'),
    ]
 
    VENDOR_PROJECT_TIG_ENTITY_NAME_CHOICES =[
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
        ('Total IT Global Finland OY','Total IT Global Finland OY'),
        ('TOTAL IT GLOBAL POLAND Sp. z o .o','TOTAL IT GLOBAL POLAND Sp. z o .o'),
        ('Total IT Global France','Total IT Global France'),
        ('Total IT Global Company Limited','Total IT Global Company Limited'),
        ('Total IT Global Germany GMBH','Total IT Global Germany GMBH'),
        ('Total IT Norway AS','Total IT Norway AS'),
        ('TI Global Sweden AB','TI Global Sweden AB'),
        ('Total IT Global UK Limited','Total IT Global UK Limited'),
    ]
 
    VENDOR_PROJECT_TYPE_OF_WORK_CHOICES =[
        ('Workspace Infrastructure','Workspace Infrastructure'),
        ('Enterprise Infrastructure','Enterprise Infrastructure'),
    ]
 
    VENDOR_PROJECT_REGION_CHOICES =[
        ('APAC','APAC'),
        ('EMEA','EMEA'),
        ('MEA','MEA'),
        ('NA','NA'),
        ('LATAM','LATAM'),
        ('AMEA','AMEA'),
        ('ANZ','ANZ'),
    ]
 
    VENDOR_PROJECT_PAYMENT_TERMS =[
        ('NET10','NET10'),
        ('NET30','NET30'),
        ('NET45','NET45'),
        ('NET60','NET60'),
        ('NET90','NET90'),
    ]
 
    VENDOR_PROJECT_BILLING_FREQUENCY = [
        ( 'One Time','One Time'),
        ( 'Weekly','Weekly'),
        ( 'Bi Weekly','Bi Weekly'),
        ( 'Monthly','Monthly'),
        ( 'Quarterly','Quarterly'),
        ( 'Half Year','Half Year'),
        ( 'Yearly','Yearly'),
        ( 'Adhoc','Adhoc'),
    ]
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    # Vendor project Information
    vp_name = models.CharField(max_length=255) #required
    vp_status = models.CharField(max_length=64, choices=VENDOR_PROJECT_STATUS_CHOICES)
    vp_vendor_account =  models.ForeignKey(VendorAccount, on_delete=models.CASCADE, related_name='vp_vendor_account') #this will come from vendor account #required
    vp_customer_project = models.ForeignKey(CustomerProject, on_delete= models.CASCADE, related_name='vp_customer_project') #this will come from customer project #required
    vp_project_start_date = models.DateField()#required
    vp_project_end_date = models.DateField()#required
    vp_tig_entity_name = models.CharField(max_length=100, choices=VENDOR_PROJECT_TIG_ENTITY_NAME_CHOICES)#required
    vp_type_of_project = models.CharField(max_length=64, choices=VENDOR_PROJECT_TYPE_OF_WORK_CHOICES)
    vp_region = models.CharField(max_length=64, choices=VENDOR_PROJECT_REGION_CHOICES)
 
    #Billing Information
    vp_payment_terms = models.CharField(max_length=64, choices=VENDOR_PROJECT_PAYMENT_TERMS)#required
    vp_billing_frequency = models.CharField(max_length=64, choices=VENDOR_PROJECT_BILLING_FREQUENCY)
    vp_terms_and_condition = models.TextField(max_length=1024, blank=True)
 
    # system information
    vp_owner = models.CharField(max_length=255)
    record_type =models.CharField(max_length=35)
   
    def __str__(self):
        return self.vp_name
   