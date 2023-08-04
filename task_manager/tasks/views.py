from task_manager.tasks.models import Tasks
from task_manager.tasks.filters import TasksFilter
from task_manager.utils import CustomLoginRequiredMixin, ObjectCreatorRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class TasksListView(CustomLoginRequiredMixin, FilterView):
    model = Tasks
    paginate_by = 10
    ordering = ['id']
    filterset_class = TasksFilter


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Tasks
    extra_context = {'title': _('Task view')}


class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tasks
    extra_context = {'title': _('Create task'), 'button_value': _('Create')}
    success_url = reverse_lazy('tasks_list')
    template_name = 'apps_forms.html'
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tasks
    extra_context = {'title': _('Change task'), 'button_value': _('Change')}
    success_url = reverse_lazy('tasks_list')
    template_name = 'apps_forms.html'
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_message = _('Task changed successfully')


class TaskDeleteView(CustomLoginRequiredMixin, ObjectCreatorRequiredMixin,
                     SuccessMessageMixin, DeleteView):
    model = Tasks
    extra_context = {'title': _('Deleting task')}
    success_url = reverse_lazy('tasks_list')
    template_name = 'confirm_delete.html'
    success_message = _('Task deleted successfully')
    creator_required_error_message = _('The task can only be deleted by its author.')

    def get_object_creator(self):
        return self.get_object().author
