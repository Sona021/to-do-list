from django.db import models


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=45)
    task_description = models.CharField(max_length = 100)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name