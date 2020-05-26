from django.db import models


class Reminder(models.Model):
    issued_date = models.DateTimeField('date created')
    text = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.text
