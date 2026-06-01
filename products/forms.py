from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for submitting a product review."""
    class Meta:
        model  = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating':  forms.Select(attrs={'class': 'form-select w-auto'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your review...'}),
        }
