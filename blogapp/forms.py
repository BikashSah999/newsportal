from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message',]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                'class': 'form-control'
                }
                ),
            'last_name': forms.TextInput(
                attrs={
                'class': 'form-control'
                }
                ),
            'email': forms.TextInput(
                attrs={
                'class': 'form-control'
                }
                ),
            'message': forms.Textarea(
                attrs={
                'class': 'form-control'
                }
                ),
            }