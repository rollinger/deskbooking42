from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from school.models import School

User = get_user_model()

class Service(models.Model):
    """ 
    Service 
    """
    name    = CharField(_("Name"),max_length=255)
    school  = ForeignKey(School, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            self.school.name,
        )

class Slot(models.Model):
    """ 
    Slot 
    """
    service     = ForeignKey(Service, on_delete=models.CASCADE)
    name        = CharField(_("Name"),max_length=255)
    place_id    = CharField(_("Identification of Place"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Slot")
        verbose_name_plural = _("Slots")

    def __str__(self):
        return "%s at %s(in %s)" % (
            self.name,
            self.service.name,
            self.service.school.name
        )

class Booking(models.Model):
    """ 
    Booking 
    """
    user    = ForeignKey(User, on_delete=models.CASCADE)
    slot    = ForeignKey(Slot, on_delete=models.CASCADE)
    start   = models.DateTimeField()
    end     = models.DateTimeField()

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def school (self):
        return self.slot.service.school
    
    def service (self):
        return self.slot.service

    def __str__(self):
        return "%s booked %s at %s" % (
            self.user.name,
            self.service,
            self.school,
        )