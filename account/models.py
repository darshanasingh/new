from django.db import models


class Log(models.Model):
    username = models.CharField(max_length=10)
    email_id = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):

        return self.username












