from task_manager.statuses.models import Statuses
from task_manager.utils import CustomLoginRequiredMixin, DeleteMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class StatusesListView(CustomLoginRequiredMixin, ListView):
    model = Statuses
    paginate_by = 10
    ordering = ['id']


class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Statuses
    extra_context = {'title': _('Create status'), 'button_value': _('Create')}
    success_url = reverse_lazy('statuses_list')
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Status created successfully')


class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    extra_context = {'title': _('Change status'), 'button_value': _('Change')}
    success_url = reverse_lazy('statuses_list')
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Status changed successfully')


class StatusDeleteView(CustomLoginRequiredMixin, DeleteMixin, DeleteView):
    model = Statuses
    extra_context = {'title': _('Deleting status')}
    success_url = reverse_lazy('statuses_list')
    template_name = 'confirm_delete.html'
    success_delete_message = _('Status deleted successfully')
    error_delete_message = _('Unable to delete the status because it is being used')
