from django.contrib import admin
from .models import Exercise

# Register your models here.
@admin.register(Exercise)
class exerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'bodypart', 'equipment', 'target']
