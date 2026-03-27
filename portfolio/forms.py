from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget = forms.HiddenInput)
    
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'content', 'rating']
       