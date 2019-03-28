from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gift_type={(0,'ubrania, które nadają się do użytku'),
           (1,'ubrania, do wyrzucenia'),
           (2,'zabawki'),
           (3,'kasiążki'),
           (4,'inne')}

help={(0,'dzieciom'),
      (1,'samotnym matkom'),
      (2,'bezdomnym'),
      (3,'niepełnosprawnym'),
      (4,'osobom starszym')}

place={(0,'Niezależne'),
       (1,'Warszawa'),
       (2,'Wrocław'),
       (3,'Poznań'),
       (4,'Gdańsk')}

class Gifts(models.Model):
    type=models.IntegerField(choices=gift_type)

    def __str__(self):
        return self.type, self.institution, self.localization

class UserAddress(models.Model):
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    postcode=models.IntegerField
    phone=models.IntegerField
    data=models.DateField()
    hour=models.TimeField()
    more_info=models.CharField(blank=True, max_length=255)

class Quantity(models.Model):
    quantity = models.IntegerField

class Organization():
    name=models.CharField(max_length=255)
    city=models.IntegerField(choices=place, default=0)
    help=models.IntegerField(choices=help ,default=0)