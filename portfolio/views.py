from django.shortcuts import render, redirect
from .forms import TestimonialForm
from django.contrib import messages
from .models import Testimonial


# Create your views here.
def home_view(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'index.html', {'testimonials':testimonials})

def submit_testimonial(request):
    """Allow users to submit testimonials"""
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['honeypot']:
                return redirect('home')
            form.save()
            messages.success(request, 'Thank you for your testimonial! It will be reviewed by our team before being published.')
            return redirect('home')
    else:
        form = TestimonialForm()
    
    return render(request, 'submit_testimonial.html', {'form': form})
