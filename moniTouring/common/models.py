from django.db import models

from moniTouring.accounts.models import MoniTouringUser
from moniTouring.monitors.models import Monitor


class Review(models.Model):
    review_text = models.CharField(max_length=500, blank=False, null=False)
    stars = models.PositiveSmallIntegerField(blank=False, default=0)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    user = models.ForeignKey(to=MoniTouringUser, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('-date_time_of_publication',)