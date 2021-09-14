from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class BookingView(TemplateView):
    template_name= "booking/booking-template.html"

    # def add_booking:

    # def remove_booking:
booking_view=BookingView.as_view()