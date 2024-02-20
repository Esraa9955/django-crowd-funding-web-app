from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time', 'category','tags']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']

ImageFormSet = forms.inlineformset_factory(Project, ProjectImage, form=ImageForm, extra=3)  # Allow 3 extra image fields


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ReportForm(forms.Form):
    reason = forms.CharField(widget=forms.Textarea)        


class ReportCommentForm(forms.ModelForm):
     class Meta:
        model = ReportComment
        fields = ['comment_reason']   

class RatingForm(forms.ModelForm):
    class Meta:
        model = ProjectRating
        fields = ['rating']