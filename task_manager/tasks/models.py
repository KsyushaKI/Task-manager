from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.users.models import CustomUser


class Tasks(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Task name'),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description'),
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        related_name='statuses',
        verbose_name=_('Status'),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='authors',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='executors',
        null=True,
        blank=True,
        verbose_name=_('Executor'),
    )
    labels = models.ManyToManyField(
        Labels,
        through='TaskRelationLabel',
        blank=True,
        related_name='labels',
        verbose_name=_('Labels'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("=Task=")
        verbose_name_plural = _("=Tasks=")


class TaskRelationLabel(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
