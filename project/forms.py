from django import forms
from .models import Project, ProjectImage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']

ImageFormSet = forms.inlineformset_factory(Project, ProjectImage, form=ImageForm, extra=3)  # Allow 3 extra image fields


