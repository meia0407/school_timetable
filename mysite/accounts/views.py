from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginForm

# Create your views here.


class Top(TemplateView):
    template_name = 'accounts/top.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/logout.html'


class CustomUserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
