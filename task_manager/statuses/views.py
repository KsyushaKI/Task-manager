from task_manager.statuses.models import Statuses
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class AuthenticatedRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.warning(
                self.request,
                _('You are not authenticated! Please log in.'),
                extra_tags='danger',
            )
        return redirect(self.login_url)


class StatusesListView(AuthenticatedRequiredMixin, ListView):
    
    model = Statuses
    login_url = '/login/'
    paginate_by = 10


class StatusCreateView(AuthenticatedRequiredMixin, SuccessMessageMixin, CreateView):

    model = Statuses
    extra_context = {'title': _('Create status'), 'button_value': _('Create')}
    success_url = reverse_lazy('statuses_list')
    login_url = '/login/'
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Status created successfully')


class StatusUpdateView(AuthenticatedRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Statuses
    extra_context = {'title': _('Change status'), 'button_value': _('Change')}
    success_url = reverse_lazy('statuses_list')
    login_url = '/login/'
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Status changed successfully')


class StatusDeleteView(AuthenticatedRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Statuses
    extra_context = {'title': _('Deleting status')}
    success_url = reverse_lazy('statuses_list')
    login_url = '/login/'
    template_name = 'confirm_delete.html'
    success_message = _('Status deleted successfully')
