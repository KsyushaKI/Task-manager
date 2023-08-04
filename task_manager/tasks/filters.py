from task_manager.labels.models import Labels
from task_manager.tasks.models import Tasks
from django.utils.translation import gettext_lazy as _
from django import forms
import django_filters


class TasksFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(label=_('Label'), queryset=Labels.objects.all())
    author = django_filters.BooleanFilter(
        method='filter_self_tasks',
        widget=forms.CheckboxInput,
        label=_('Only own tasks')
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor']
