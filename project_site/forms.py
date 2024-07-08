from django import forms
from .models import ProjectSite
from projects.models import CustomerProject

class ProjectSiteForm(forms.ModelForm):
        
    ps_project_uuid = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ProjectSite
        fields = [
            'ps_name',
            'ps_site_coordinator',
            'ps_working_days',
            'ps_project_uuid',
            'ps_business_start_time',
            'ps_business_end_time',
            'ps_address',
            'ps_city',
            'ps_state',
            'ps_country',
            'ps_ZIP_postal_Code',
            'ps_ZIP_site_classification',
            'ps_ZIP_site_code',
            'ps_ZIP_gps_coordinates',
            'ps_number_of_assets',
            'ps_number_of_users',
        ]


    # def clean_ps_project_uuid(self):
    #     ps_project_uuid = self.cleaned_data.get('ps_project_uuid')
    #     if not ps_project_uuid:
    #         raise forms.ValidationError('This field is required.')
    #     try:
    #         ps_project = CustomerProject.objects.get(id=ps_project_uuid)
    #     except CustomerProject.DoesNotExist:
    #         raise forms.ValidationError('Invalid project selected.')
    #     return ps_project

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_ps_project_uuid(self):
        ps_project_uuid = self.cleaned_data.get('ps_project_uuid')
        
        # Skip validation if the instance already has ps_project_uuid
        if not ps_project_uuid and self.instance and self.instance.ps_project_uuid:
            return self.instance.ps_project_uuid
        
        if not ps_project_uuid:
            raise forms.ValidationError('This field is required.')
        
        try:
            ps_project = CustomerProject.objects.get(id=ps_project_uuid)
        except CustomerProject.DoesNotExist:
            raise forms.ValidationError('Invalid project selected.')
        
        return ps_project_uuid