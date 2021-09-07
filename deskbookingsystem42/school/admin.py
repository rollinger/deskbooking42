from .models import School, Key, Configuration
from django.contrib import admin

# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = [ "name", ]
    search_fields = ["name"]

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = [ "school", "key", "value" ]
    autocomplete_fields = ["school", "key"]
