from django.db import models


class Topic(models.Model):
    issued_date = models.DateTimeField('date created')
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class List(models.Model):
    list_text = models.CharField(max_length=200)
    topic_title = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_text

