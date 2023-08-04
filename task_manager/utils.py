from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.db.models import ProtectedError


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_required_error_message = _('You are not authenticated! Please log in.')

    def handle_no_permission(self):
        messages.warning(self.request, self.login_required_error_message, extra_tags='danger')
        return redirect('login')


class DeleteMixin():
    success_delete_message = _('Object deleted successfully')
    error_delete_message = _('Unable to delete the object because it is being used')

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, self.success_delete_message)
            return redirect(self.success_url)

        except ProtectedError:
            messages.warning(self.request, self.error_delete_message, extra_tags='danger')
            return redirect(self.success_url)


class ObjectCreatorRequiredMixin(AccessMixin):
    creator_required_error_message = _('You are not authorized to do this')

    def get_object_creator(self):
        return self.get_object()

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object_creator():
            messages.warning(request, self.creator_required_error_message, extra_tags='danger')
            return redirect(self.success_url)

        return super().dispatch(request, *args, **kwargs)
