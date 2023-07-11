from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class SignIn(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Successfully login'


class LogOut(SuccessMessageMixin, LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logout')
        return response
