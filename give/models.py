from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gift_type={(0,'ubrania, które nadają się do użytku'),
           (1,'ubrania, do wyrzucenia'),
           (2,'zabawki'),
           (3,'kasiążki'),
           (4,'inne')}

institutions={(0,'Dbam o Zdrowie'),
             (1,'Dla dzieci'),
             (2,'Bez domu'),
             (3,'Walka z rakiem "Yasuo mid"'),
             (4,'Mam marzenie')}

place={(0,'Niezależne'),
       (1,'Warszawa'),
       (2,'Wrocław'),
       (3,'Poznań'),
       (4,'Gdańsk')}

class Gifts(models.Model):
    type=models.IntegerField(choices=gift_type)
    quantity=models.IntegerField
    institution=models.IntegerField(choices=institutions)
    localization=models.IntegerField(choices=place, default=0)

    def __str__(self):
        return self.type, self.institution, self.localization

class UserAddress(models.Model):
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    postcode=models.IntegerField
    phone=models.IntegerField
    data=models.DateField()
    hour=models.TimeField
    more_info=models.CharField(blank=True, max_length=255)
    gift=models.OneToOneField( User , on_delete=models.CASCADE, primary_key=True,)