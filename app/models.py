from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):

    status = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', "Completed"),
    )
    
    item = models.CharField(max_length=500)
    status = models.CharField(choices=status, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
