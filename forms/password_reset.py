from django import forms

class PasswordResetForm(forms.Form):
    current_password = forms.CharField()
    new_password = forms.CharField()
    retype_password = forms.CharField()

