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

    paginate_by = 10
    model = CustomUser


class SignUpView(SuccessMessageMixin, CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
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
    success_url = reverse_lazy('users_list')
    login_url = '/login/'
    template_name = 'users/update.html'
    fields = ['first_name', 'last_name', 'username']
    success_message = _('User changed successfully')


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):

    model = CustomUser
    success_url = reverse_lazy('users_list')
    template_name = 'users/password_change.html'
    success_message = _('Password changed successfully')


class UserDeleteView(UserRequiredMixin, SuccessMessageMixin, DeleteView):

    model = CustomUser
    success_url = reverse_lazy('users_list')
    login_url = '/login/'
    template_name = 'users/confirm_delete.html'
    success_message = _('User deleted successfully')
