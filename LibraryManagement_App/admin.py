from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(AdminLogin)
class AdminLoginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AdminLogin._meta.get_fields()]

@admin.register(StudentLogin)
class AdminLoginAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentLogin._meta.get_fields()]


@admin.register(BookDetails)
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BookDetails._meta.get_fields()]