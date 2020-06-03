from django.contrib import admin
from .models import MyProject
# Register your models here.

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
  list_display = ['image', 'urlProject', 'nameProject']