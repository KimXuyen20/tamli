from django import forms
from .models import Doctor
from accounts.validators import allow_only_images_validator



class DoctorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = Doctor
        fields = ['doctor_name', 'doctor_license']