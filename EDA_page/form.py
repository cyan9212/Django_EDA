from django import forms
from .models import Features

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields =('feature1', 'feature2', 'hue')