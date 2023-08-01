from task_manager.users.forms import CustomUserCreationForm
from task_manager.users.models import CustomUser
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UsersListView(ListView):
   
    model = CustomUser
    paginate_by = 10


class SignUpView(SuccessMessageMixin, CreateView):

    form_class = CustomUserCreationForm
    extra_context = {'title': _('Registration'), 'button_value': _('Sign Up')}
    success_url = reverse_lazy('login')
    template_name = 'apps_forms.html'
    success_message = _('User successfully registered')


class UserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(
                request,
                _('You are not authenticated! Please log in.'),
                extra_tags='danger',
            )
            return redirect('login')

        if request.user.is_authenticated:
            if request.user != self.get_object():
                messages.warning(
                    request,
                    _('You do not have permission to change another user.'),
                    extra_tags='danger',
                )
                return redirect('users_list')

        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UserRequiredMixin, SuccessMessageMixin, UpdateView):

    model = CustomUser
    extra_context = {'title': _('User change'), 'button_value': _('Change'), 'additional_info': True}
    success_url = reverse_lazy('users_list')
    login_url = '/login/'
    template_name = 'apps_forms.html'
    fields = ['first_name', 'last_name', 'username']
    success_message = _('User changed successfully')


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):

    model = CustomUser
    extra_context = {'title': _('Change password'), 'button_value': _('Change')}
    success_url = reverse_lazy('users_list')
    template_name = 'apps_forms.html'
    success_message = _('Password changed successfully')


class UserDeleteView(UserRequiredMixin, SuccessMessageMixin, DeleteView):

    model = CustomUser
    extra_context = {'title': _('Deleting user')}
    success_url = reverse_lazy('users_list')
    login_url = '/login/'
    template_name = 'confirm_delete.html'
    success_message = _('User deleted successfully')
