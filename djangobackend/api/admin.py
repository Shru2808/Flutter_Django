from django.contrib import admin

# Register your models here.
from .models import candidates

@admin.register(candidates)
class CanAdmin(admin.ModelAdmin):
    list_display = ['id','canname','email']
    