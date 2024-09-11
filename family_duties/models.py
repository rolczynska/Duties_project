from django.db import models
from profiles.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',
                                    blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-created']

