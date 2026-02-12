from django.contrib import admin
from .models import Organization
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
