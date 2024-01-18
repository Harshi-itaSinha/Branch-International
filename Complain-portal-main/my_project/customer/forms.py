from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'phone_number', 'email', 'order_date', 'product_category', 'product_name', 'question']
