from django.db import models
import uuid
from multiselectfield import MultiSelectField

from cities_light.models import Country, Region
from projects.models import CustomerProject

class ProjectSite(models.Model):

    PROJECT_SITE_CLASSIFICATION_CHOICES = [
        ('Metro','Metro'),
        ('Rural','Rural'),
        ('Regional','Regional'),
    ]

    PROJECT_SITE_WORKING_DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
   
    PROJECT_SITE_BUSINESS_START_TIME = [
        ('12:00 AM' , '12:00 AM'),
        ('12:15 AM' , '12:15 AM'),
        ('12:30 AM' , '12:30 AM'),
        ('12:45 AM' , '12:45 AM'),
       
        ('01:00 AM' , '01:00 AM'),
        ('01:15 AM' , '01:15 AM'),
        ('01:30 AM' , '01:30 AM'),
        ('01:45 AM' , '01:45 AM'),
       
        ('02:00 AM' , '02:00 AM'),
        ('02:15 AM' , '02:15 AM'),
        ('02:30 AM' , '02:30 AM'),
        ('02:45 AM' , '02:45 AM'),
       
        ('03:00 AM' , '03:00 AM'),
        ('03:15 AM' , '03:15 AM'),
        ('03:30 AM' , '03:30 AM'),
        ('03:45 AM' , '03:45 AM'),
       
        ('04:00 AM' , '04:00 AM'),
        ('04:15 AM' , '04:15 AM'),
        ('04:30 AM' , '04:30 AM'),
        ('04:45 AM' , '04:45 AM'),
       
        ('05:00 AM' , '05:00 AM'),
        ('05:15 AM' , '05:15 AM'),
        ('05:30 AM' , '05:30 AM'),
        ('05:45 AM' , '05:45 AM'),
       
        ('06:00 AM' , '06:00 AM'),
        ('06:15 AM' , '06:15 AM'),
        ('06:30 AM' , '06:30 AM'),
        ('06:45 AM' , '06:45 AM'),
       
        ('07:00 AM' , '07:00 AM'),
        ('07:15 AM' , '07:15 AM'),
        ('07:30 AM' , '07:30 AM'),
        ('07:45 AM' , '07:45 AM'),
       
        ('08:00 AM' , '08:00 AM'),
        ('08:15 AM' , '08:15 AM'),
        ('08:30 AM' , '08:30 AM'),
        ('08:45 AM' , '08:45 AM'),
       
        ('09:00 AM' , '09:00 AM'),
        ('09:15 AM' , '09:15 AM'),
        ('09:30 AM' , '09:30 AM'),
        ('09:45 AM' , '09:45 AM'),
       
        ('10:00 AM' , '10:00 AM'),
        ('10:15 AM' , '10:15 AM'),
        ('10:30 AM' , '10:30 AM'),
        ('10:45 AM' , '10:45 AM'),
       
        ('11:00 AM' , '11:00 AM'),
        ('11:15 AM' , '11:15 AM'),
        ('11:30 AM' , '11:30 AM'),
        ('11:45 AM' , '11:45 AM'),
       
        ('12:00 PM' , '12:00 PM'),
        ('12:15 PM' , '12:15 PM'),
        ('12:30 PM' , '12:30 PM'),
        ('12:45 PM' , '12:45 PM'),
       
        ('01:00 PM' , '01:00 PM'),
        ('01:15 PM' , '01:15 PM'),
        ('01:30 PM' , '01:30 PM'),
        ('01:45 PM' , '01:45 PM'),
       
        ('02:00 PM' , '02:00 PM'),
        ('02:15 PM' , '02:15 PM'),
        ('02:30 PM' , '02:30 PM'),
        ('02:45 PM' , '02:45 PM'),
       
        ('03:00 PM' , '03:00 PM'),
        ('03:15 PM' , '03:15 PM'),
        ('03:30 PM' , '03:30 PM'),
        ('03:45 PM' , '03:45 PM'),
       
        ('04:00 PM' , '04:00 PM'),
        ('04:15 PM' , '04:15 PM'),
        ('04:30 PM' , '04:30 PM'),
        ('04:45 PM' , '04:45 PM'),
       
        ('05:00 PM' , '05:00 PM'),
        ('05:15 PM' , '05:15 PM'),
        ('05:30 PM' , '05:30 PM'),
        ('05:45 PM' , '05:45 PM'),
       
        ('06:00 PM' , '06:00 PM'),
        ('06:15 PM' , '06:15 PM'),
        ('06:30 PM' , '06:30 PM'),
        ('06:45 PM' , '06:45 PM'),
       
        ('07:00 PM' , '07:00 PM'),
        ('07:15 PM' , '07:15 PM'),
        ('07:30 PM' , '07:30 PM'),
        ('07:45 PM' , '07:45 PM'),
       
        ('08:00 PM' , '08:00 PM'),
        ('08:15 PM' , '08:15 PM'),
        ('08:30 PM' , '08:30 PM'),
        ('08:45 PM' , '08:45 PM'),
       
        ('09:00 PM' , '09:00 PM'),
        ('09:15 PM' , '09:15 PM'),
        ('09:30 PM' , '09:30 PM'),
        ('09:45 PM' , '09:45 PM'),
       
        ('10:00 PM' , '10:00 PM'),
        ('10:15 PM' , '10:15 PM'),
        ('10:30 PM' , '10:30 PM'),
        ('10:45 PM' , '10:45 PM'),
       
        ('11:00 PM' , '11:00 PM'),
        ('11:15 PM' , '11:15 PM'),
        ('11:30 PM' , '11:30 PM'),
        ('11:45 PM' , '11:45 PM'),
 
 
    ]
   
    PROJECT_SITE_BUSINESS_END_TIME = [
         ('12:00 AM' , '12:00 AM'),
        ('12:15 AM' , '12:15 AM'),
        ('12:30 AM' , '12:30 AM'),
        ('12:45 AM' , '12:45 AM'),
       
        ('01:00 AM' , '01:00 AM'),
        ('01:15 AM' , '01:15 AM'),
        ('01:30 AM' , '01:30 AM'),
        ('01:45 AM' , '01:45 AM'),
       
        ('02:00 AM' , '02:00 AM'),
        ('02:15 AM' , '02:15 AM'),
        ('02:30 AM' , '02:30 AM'),
        ('02:45 AM' , '02:45 AM'),
       
        ('03:00 AM' , '03:00 AM'),
        ('03:15 AM' , '03:15 AM'),
        ('03:30 AM' , '03:30 AM'),
        ('03:45 AM' , '03:45 AM'),
       
        ('04:00 AM' , '04:00 AM'),
        ('04:15 AM' , '04:15 AM'),
        ('04:30 AM' , '04:30 AM'),
        ('04:45 AM' , '04:45 AM'),
       
        ('05:00 AM' , '05:00 AM'),
        ('05:15 AM' , '05:15 AM'),
        ('05:30 AM' , '05:30 AM'),
        ('05:45 AM' , '05:45 AM'),
       
        ('06:00 AM' , '06:00 AM'),
        ('06:15 AM' , '06:15 AM'),
        ('06:30 AM' , '06:30 AM'),
        ('06:45 AM' , '06:45 AM'),
       
        ('07:00 AM' , '07:00 AM'),
        ('07:15 AM' , '07:15 AM'),
        ('07:30 AM' , '07:30 AM'),
        ('07:45 AM' , '07:45 AM'),
       
        ('08:00 AM' , '08:00 AM'),
        ('08:15 AM' , '08:15 AM'),
        ('08:30 AM' , '08:30 AM'),
        ('08:45 AM' , '08:45 AM'),
       
        ('09:00 AM' , '09:00 AM'),
        ('09:15 AM' , '09:15 AM'),
        ('09:30 AM' , '09:30 AM'),
        ('09:45 AM' , '09:45 AM'),
       
        ('10:00 AM' , '10:00 AM'),
        ('10:15 AM' , '10:15 AM'),
        ('10:30 AM' , '10:30 AM'),
        ('10:45 AM' , '10:45 AM'),
       
        ('11:00 AM' , '11:00 AM'),
        ('11:15 AM' , '11:15 AM'),
        ('11:30 AM' , '11:30 AM'),
        ('11:45 AM' , '11:45 AM'),
       
        ('12:00 PM' , '12:00 PM'),
        ('12:15 PM' , '12:15 PM'),
        ('12:30 PM' , '12:30 PM'),
        ('12:45 PM' , '12:45 PM'),
       
        ('01:00 PM' , '01:00 PM'),
        ('01:15 PM' , '01:15 PM'),
        ('01:30 PM' , '01:30 PM'),
        ('01:45 PM' , '01:45 PM'),
       
        ('02:00 PM' , '02:00 PM'),
        ('02:15 PM' , '02:15 PM'),
        ('02:30 PM' , '02:30 PM'),
        ('02:45 PM' , '02:45 PM'),
       
        ('03:00 PM' , '03:00 PM'),
        ('03:15 PM' , '03:15 PM'),
        ('03:30 PM' , '03:30 PM'),
        ('03:45 PM' , '03:45 PM'),
       
        ('04:00 PM' , '04:00 PM'),
        ('04:15 PM' , '04:15 PM'),
        ('04:30 PM' , '04:30 PM'),
        ('04:45 PM' , '04:45 PM'),
       
        ('05:00 PM' , '05:00 PM'),
        ('05:15 PM' , '05:15 PM'),
        ('05:30 PM' , '05:30 PM'),
        ('05:45 PM' , '05:45 PM'),
       
        ('06:00 PM' , '06:00 PM'),
        ('06:15 PM' , '06:15 PM'),
        ('06:30 PM' , '06:30 PM'),
        ('06:45 PM' , '06:45 PM'),
       
        ('07:00 PM' , '07:00 PM'),
        ('07:15 PM' , '07:15 PM'),
        ('07:30 PM' , '07:30 PM'),
        ('07:45 PM' , '07:45 PM'),
       
        ('08:00 PM' , '08:00 PM'),
        ('08:15 PM' , '08:15 PM'),
        ('08:30 PM' , '08:30 PM'),
        ('08:45 PM' , '08:45 PM'),
       
        ('09:00 PM' , '09:00 PM'),
        ('09:15 PM' , '09:15 PM'),
        ('09:30 PM' , '09:30 PM'),
        ('09:45 PM' , '09:45 PM'),
       
        ('10:00 PM' , '10:00 PM'),
        ('10:15 PM' , '10:15 PM'),
        ('10:30 PM' , '10:30 PM'),
        ('10:45 PM' , '10:45 PM'),
       
        ('11:00 PM' , '11:00 PM'),
        ('11:15 PM' , '11:15 PM'),
        ('11:30 PM' , '11:30 PM'),
        ('11:45 PM' , '11:45 PM'),
    ]
 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    # Site Information
    ps_name = models.CharField(max_length=255,)
    ps_site_coordinator = models.CharField(max_length=255 , blank=True)
    ps_working_days = MultiSelectField(choices=PROJECT_SITE_WORKING_DAYS_CHOICES, max_choices=7, max_length=1024, blank=True)
    ps_project = models.ForeignKey(CustomerProject, on_delete=models.CASCADE, related_name='ps_project') #this project will be selected from suggestions of Customer Project
    ps_business_start_time = models.CharField(max_length=255, blank=True, choices=PROJECT_SITE_BUSINESS_START_TIME)
    ps_business_end_time = models.CharField(max_length=255, blank=True, choices=PROJECT_SITE_BUSINESS_END_TIME)
   
 
    # Site Address Information
    ps_address = models.TextField(max_length=250, blank=True)
    ps_city = models.CharField(max_length=255)
    ps_state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='ps_state') # this data comes from Country
    ps_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='ps_country')# this data comes from State
    ps_ZIP_postal_Code = models.CharField(max_length=64, blank=True)
    ps_ZIP_site_classification = models.CharField(max_length=64, blank=True, choices=PROJECT_SITE_CLASSIFICATION_CHOICES)
    ps_ZIP_site_code = models.CharField(max_length=64, blank=True)
    ps_ZIP_gps_coordinates = models.CharField(max_length=64, blank=True)
   
    # other information
    ps_number_of_assets = models.CharField(max_length=255, blank=True)
    ps_number_of_users = models.CharField(max_length=255, blank=True)
    
    # Model information 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated_by')

    def save_working_days(self, days_list):
        # Convert list of days to comma-separated string
        self.ps_working_days = ','.join(days_list)

    def get_working_days(self):
        # Convert comma-separated string to list of days
        return self.ps_working_days.split(',') if self.ps_working_days else []

    def __str__(self):
        return self.ps_name