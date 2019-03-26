from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .models import Gifts,UserAddress
# Create your views here.

def main(request):
    return render(request,'index.html')

class Gifts(View):
    def get(self,request):
        return render(request,'form.html')

    def post(self,request):
        product=request.POST['product']
        bags=request.POST['bags']
        localization=request.POST['localization']
        help=request.POST['help']
        organization=request.POST['organization']
        address=request.POST['address']
        city=request.POST['city']
        postcode=request.POST['postcode']
        phone=request.POST['phone']
        data=request.POST['data']
        time=request.POST['time']
        more_info=request.POST['more_info']
        gift=Gifts.objects.create(type=product,quantity=bags,institution=organization,localization=localization)
        addres=UserAddress.objects.create(address=address,city=city,postcode=postcode,phone=phone,data=data,hour=time,more_info=more_info)
        return render(request,'form.html',{'gift':gift, 'address':addres})