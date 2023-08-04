from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser
from task_manager.utils import CustomLoginRequiredMixin, ObjectCreatorRequiredMixin, DeleteMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class UsersListView(ListView):
    model = CustomUser
    paginate_by = 10
    ordering = ['id']


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    extra_context = {'title': _('Registration'), 'button_value': _('Sign Up')}
    success_url = reverse_lazy('login')
    template_name = 'apps_forms.html'
    success_message = _('User successfully registered')


class UserUpdateView(CustomLoginRequiredMixin, ObjectCreatorRequiredMixin,
                     SuccessMessageMixin, UpdateView):
    model = CustomUser
    extra_context = {'title': _('User change'), 'button_value': _('Change'), 'extra_info': True}
    success_url = reverse_lazy('users_list')
    template_name = 'apps_forms.html'
    fields = ['first_name', 'last_name', 'username']
    success_message = _('User changed successfully')
    creator_required_error_message = _('You do not have permission to change another user.')


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    model = CustomUser
    extra_context = {'title': _('Change password'), 'button_value': _('Change')}
    success_url = reverse_lazy('users_list')
    template_name = 'apps_forms.html'
    success_message = _('Password changed successfully')


class UserDeleteView(CustomLoginRequiredMixin, ObjectCreatorRequiredMixin, DeleteMixin, DeleteView):
    model = CustomUser
    extra_context = {'title': _('Deleting user')}
    success_url = reverse_lazy('users_list')
    template_name = 'confirm_delete.html'
    creator_required_error_message = _('You do not have permission to delete another user.')
    success_delete_message = _('User deleted successfully')
    error_delete_message = _('Unable to delete the user because it is being used')
