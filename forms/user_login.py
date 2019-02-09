from django.contrib.auth import forms

class userloginform(forms.AuthenticationForm):
    def confirm_login_allowed(self,user):
        if not user.is_active:
            raise forms.ValidationError(
                _("Your account is flagged as currently inactive."),
                code='inactive'
            
            )