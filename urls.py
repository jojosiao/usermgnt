from django.urls import path, include
from django.conf import settings as SETTINGS
# to obtain greater control in user authentication
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# as per the docs say, you may not need to use the built-in views but not having to write all the forms for this functionality
# https://docs.djangoproject.com/en/2.1/topics/auth/default/#built-in-auth-forms

from .forms.user_login import userloginform
#from .forms.password_change import passwordchangeform
from .forms.password_reset import forgotpasswordform


urlpatterns = [
    
    # I think using auth_views classes will help us to do coding easier and faster.
    path('register/',TemplateView.as_view(template_name="usermgnt/register.html"), name="signup"),
    
    path('login/',auth_views.LoginView.as_view(
            template_name="usermgnt/login.html",
            authentication_form=userloginform,
            redirect_authenticated_user = True
        ),
        name="login"
    ),

    path('password_change/', auth_views.PasswordChangeView.as_view(
            template_name = "usermgnt/password_change_form.html",
            success_url = SETTINGS.DEFAULT_HOMEPAGE,
        ),
        name = "usermgnt-password_change"
    ),

    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(
            template_name = "usermgnt/password_change_done.html"
        )
    ),

    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name = "usermgnt/password_reset_form.html",
            form_class = forgotpasswordform,
            success_url = SETTINGS.DEFAULT_HOMEPAGE,
            email_template_name = "usermgnt/emails/password_reset_email.html",
            subject_template_name = "usermgnt/password_reset_subject.txt",

        ),
        name = "usermgnt-password_reset"
    ),

    path('password_reset_confirm/<uuid:uidb64>/<str:token>/',auth_views.PasswordResetConfirmView.as_view(
            template_name = "usermgnt/password_reset_confirm_form.html",
            

        ),
        name = "usermgnt-password_reset_confirm"
    ),

    path('logout/',auth_views.LogoutView.as_view(template_name="usermgnt/logout.html"), name="logout"),
    
]