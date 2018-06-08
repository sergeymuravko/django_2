from django.db import models

# Create your models here.


class Poll(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"
