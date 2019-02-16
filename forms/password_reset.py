from django import forms

class forgotpasswordform(forms.Form):
    current_password = forms.CharField()
    new_password = forms.CharField()
    retype_password = forms.CharField()

