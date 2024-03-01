from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import SignInForm, LoginForm

# Create your views here.


class Index(TemplateView):
    template_name = 'accounts/index.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/logout.html'


class CustomUserCreateView(CreateView):
    form_class = SignInForm
    template_name = 'accounts/signin.html'
    success_url = reverse_lazy('school:index')
