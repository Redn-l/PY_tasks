from django.db import models
from django.contrib.auth.models import User

owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ])
    due_date = models.DateField()

    def __str__(self):
        return self.title
