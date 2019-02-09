from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class passwordchangeform(PasswordChangeForm, forms):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)