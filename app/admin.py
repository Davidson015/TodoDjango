from django.contrib import admin
from app.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
  list_display = [
    "title",
    "status",
    "created_at",
    "updated_at",
    "is_updated",
  ]