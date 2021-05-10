from django.db import models
from django.contrib.auth import get_user_model

from projects.models import Project
from utils.models import AbstractTableMeta


class StudentSubmission(AbstractTableMeta, models.Model):
    student = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
                                on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=255)
    feedback = models.TextField(blank=True, default='')
    approved = models.BooleanField(default=False)
