<<<<<<< HEAD

=======
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c
# Django
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin, LoginAjaxMixin
# Project
<<<<<<< HEAD
from .forms import CustomUserCreationForm, CustomAuthenticationForm
=======
from .forms import CustomUserCreationForm
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c


class SignUp(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('login')

<<<<<<< HEAD

class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'account/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('post_list')
=======
>>>>>>> 140d16638259d6faea57a2334bd2d992bd24bf3c
