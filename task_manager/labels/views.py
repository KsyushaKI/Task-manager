from task_manager.labels.models import Labels
from task_manager.utils import CustomLoginRequiredMixin, DeleteMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LabelsListView(CustomLoginRequiredMixin, ListView):
    model = Labels
    paginate_by = 10
    ordering = ['id']


class LabelCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Labels
    extra_context = {'title': _('Create label'), 'button_value': _('Create')}
    success_url = reverse_lazy('labels_list')
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Label created successfully')


class LabelUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    extra_context = {'title': _('Change label'), 'button_value': _('Change')}
    success_url = reverse_lazy('labels_list')
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Label changed successfully')


class LabelDeleteView(CustomLoginRequiredMixin, DeleteMixin, DeleteView):
    model = Labels
    extra_context = {'title': _('Deleting label')}
    success_url = reverse_lazy('labels_list')
    template_name = 'confirm_delete.html'
    success_delete_message = _('Label deleted successfully')
    error_delete_message = _('Unable to delete the label because it is being used')
