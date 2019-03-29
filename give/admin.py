from django.contrib import admin
from .models import Gifts,Organization,UserAddress,Quantity

class GiftAdmin(admin.ModelAdmin):
    list_display = ('id','type')
admin.site.register(Gifts, GiftAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name','city','help')
admin.site.register(Organization, OrganizationAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id','address','city','postcode','phone','data','hour','more_info')
admin.site.register(UserAddress, UserAddressAdmin)

class QuantityAdmin(admin.ModelAdmin):
    list_display = ('id','quantity')
admin.site.register(Quantity, QuantityAdmin)