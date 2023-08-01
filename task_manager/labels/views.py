from task_manager.labels.models import Labels
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


class LabelsListView(AuthenticatedRequiredMixin, ListView):
    
    model = Labels
    login_url = '/login/'
    paginate_by = 10


class LabelCreateView(AuthenticatedRequiredMixin, SuccessMessageMixin, CreateView):

    model = Labels
    extra_context = {'title': _('Create label'), 'button_value': _('Create')}
    success_url = reverse_lazy('labels_list')
    login_url = '/login/'
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Label created successfully')


class LabelUpdateView(AuthenticatedRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Labels
    extra_context = {'title': _('Change label'), 'button_value': _('Change')}
    success_url = reverse_lazy('labels_list')
    login_url = '/login/'
    template_name = 'apps_forms.html'
    fields = ['name']
    success_message = _('Label changed successfully')


class LabelDeleteView(AuthenticatedRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Labels
    extra_context = {'title': _('Deleting label')}
    success_url = reverse_lazy('labels_list')
    login_url = '/login/'
    template_name = 'confirm_delete.html'
    success_message = _('Label deleted successfully')
