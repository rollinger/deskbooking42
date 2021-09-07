from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class School(models.Model):
    name    = CharField(max_length=255)

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return _("School: %s") % (self.name)

class Key(models.Model):
    """ Key for the Configuration
    TODO: We need to create a fixture with the basic configs...!
    """
    name    = CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _("Key")
        verbose_name_plural = _("Keys")

    def __str__(self):
        return self.name

class Configuration(models.Model):
    school  = models.ForeignKey(School, related_name="config_list", on_delete=models.CASCADE)
    key     = models.ForeignKey(Key, related_name='config_list', on_delete=models.CASCADE)
    value   = CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _("Configuration")
        verbose_name_plural = _("Configurations")

    def __str__(self):
        return _("%s: %s => %s") % (self.school.name, self.key.name, self.value)