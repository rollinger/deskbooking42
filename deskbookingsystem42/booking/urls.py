from django.urls import path
from deskbookingsystem42.booking.views import (
    booking_view,
)

app_name = "booking"
urlpatterns = [
    path("", view=booking_view, name="overview"),
]