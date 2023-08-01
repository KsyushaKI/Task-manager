from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):

    template_name = 'index.html'


class SignIn(SuccessMessageMixin, LoginView):

    template_name = 'apps_forms.html'
    extra_context = {'title': _('Authorization'), 'button_value': _('Log In')}
    success_message = _('Successfully login')


class LogOut(SuccessMessageMixin, LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, _('Successfully logout'))
        return response
