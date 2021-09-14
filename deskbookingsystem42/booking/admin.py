from .models import Slot, Service, Booking
from django.contrib import admin

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["user", "slot", "start", "end"]
    search_fields = ["user", "slot", "service", "school"]

