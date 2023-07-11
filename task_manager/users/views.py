from .forms import CustomUserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UsersListView(ListView):
    paginate_by = 25
    model = CustomUser


class SignUpView(SuccessMessageMixin, CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    success_message = 'Пользователь успешно зарегистрирован'


class UserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(
                request,
                'Вы не авторизованы! Пожалуйста, выполните вход.',
                extra_tags='danger',
            )
            return self.handle_no_permission()

        if request.user.is_authenticated:
            if request.user != self.get_object():
                messages.warning(
                    request,
                    'У вас нет прав для изменения другого пользователя.',
                    extra_tags='danger',
                )
                return redirect('users_list')

        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UserRequiredMixin, SuccessMessageMixin, UpdateView):

    model = CustomUser
    success_url = reverse_lazy('users_list')
    template_name = 'users/update.html'
    login_url = '/login/'
    fields = ['first_name', 'last_name', 'username']
    success_message = 'Пользователь успешно изменен'


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('users_list')
    template_name = 'users/password_change.html'
    success_message = 'Пароль успешно изменен'
    model = CustomUser


class UserDeleteView(UserRequiredMixin, SuccessMessageMixin, DeleteView):

    model = CustomUser
    success_url = reverse_lazy('users_list')
    template_name = 'users/confirm_delete.html'
    login_url = '/login/'
    redirect_field_name = 'login'
    success_message = 'Пользователь успешно удален'
