from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey
from django.db.models.deletion import SET_NULL
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Role(Model):
    """Default role for 42users."""
    name = CharField(max_length=200, blank=True, default=False)

class User(AbstractUser):
    """Default user for DeskBookingSystem42."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = ForeignKey(Role, null=True, blank=True, on_delete=SET_NULL)
    school = None #@Philipp  

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
