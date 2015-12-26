from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.user_name

    def getClass(self):
        return "User"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length = 50)
    priority = models.IntegerField()
    description = models.CharField(max_length = 300)

    def __str__(self):
        return self.task_name

    def getClass(self):
        return "Task"
