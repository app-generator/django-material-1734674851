# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Item(models.Model):

    #__Item_FIELDS__
    itemid = models.IntegerField(null=True, blank=True)
    itemname = models.CharField(max_length=255, null=True, blank=True)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")


class Country(models.Model):

    #__Country_FIELDS__
    countryid = models.IntegerField(null=True, blank=True)
    countryname = models.CharField(max_length=255, null=True, blank=True)

    #__Country_FIELDS__END

    class Meta:
        verbose_name        = _("Country")
        verbose_name_plural = _("Country")


class City(models.Model):

    #__City_FIELDS__
    cityid = models.IntegerField(null=True, blank=True)
    cityname = models.CharField(max_length=255, null=True, blank=True)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)

    #__City_FIELDS__END

    class Meta:
        verbose_name        = _("City")
        verbose_name_plural = _("City")



#__MODELS__END
