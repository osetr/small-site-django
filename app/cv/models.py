from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Post(models.Model):
    full_name = models.CharField(verbose_name="Name",
                                 max_length=35,
                                 unique=True)
    date = models.DateTimeField(default=datetime.now(), editable=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    link = models.URLField(verbose_name="CV link", max_length=128)

    def __str__(self):
        return "%s by %s" % (self.link, self.full_name)
