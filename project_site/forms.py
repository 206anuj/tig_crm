from django import forms
from .models import ProjectSite


class ProjectSiteForm(forms.ModelForm):
    
    class Meta:
        model = ProjectSite
        fields = "__all__"
