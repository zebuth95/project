from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", blank=True)

    def __str__(self):
        return str(self.name)

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=512)
    status = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects", blank=True)

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    message = models.CharField(max_length=512)
    creation_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments", blank=True)

    def __str__(self):
        return str(self.id)
