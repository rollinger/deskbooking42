from django.shortcuts import render
from django.views.generic.base import TemplateView
from allauth.account.forms import LoginForm, SignupForm

# Create your views here.
class BookingView(TemplateView):
    template_name= "booking/booking-template.html"
    context= {
        'LoginForm': LoginForm(),
        'SignupForm': SignupForm()
    }

    # def add_booking:

    # def remove_booking:
booking_view=BookingView.as_view()