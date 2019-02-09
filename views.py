from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    pass


# def login(request,LoginView):
#     template_name = "usermgnt/login.html"
#     redirect_field_name = ""
#     authentication_form = AuthenticationForm
#     redirect_authenticated_user = True


def logout(request, LogoutView):
    template_name = "usermgnt/logout.html"
    