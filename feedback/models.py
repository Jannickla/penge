from django.db import models
from accounts.models import Account


class Feedback(models.Model):
    subject = models.CharField(max_length=130)
    feedback_description = models.TextField(max_length=2500)
    overall_satisfaction = models.IntegerField(default=None, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
