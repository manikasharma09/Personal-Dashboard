from django.db import models


class Todo(models.Model):
    added_date = models.DateTimeField('date created')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text