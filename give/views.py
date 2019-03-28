from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Gifts,UserAddress,User,Quantity,Organization
# Create your views here.
@login_required
def main(request):
    return render(request,'index.html')

class SignIn(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        name = request.POST['login']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=name,password=password,email=email)
        login(request, user)
        return redirect('/')

class ProductView(View):
    def get(self,request):
        return render(request,'form1.html')

    def post(self,request):
        type=request.POST['products']
        gift=Gifts.objects.create(type=type)
        request.session['Product_id'] = gift.id
        return redirect('form2/')


class QuantityView(View):
    def get(self, request):
        return render(request, 'form2.html')

    def post(self, request):
        bags = request.POST['bags']
        bags = Quantity.objects.create(quantity=bags)
        request.session['Quantity_id'] = bags.id
        return redirect('form/')


class OrganizationView(View):
    def get(self, request):
        organization=Organization.object.all()
        return render(request, 'form4.html',{'organizations':organization})

    def post(self, request):
        type = request.POST['products']
        organization = Organization.objects.create()
        request.session['Organization_id'] = organization.id
        return redirect('form5/')


class AddressView(View):
    def get(self, request):
        return render(request, 'form5.html')

    def post(self, request):
        address=request.POST['address']
        city=request.POST['city']
        postcode=request.POST['postcode']
        phone=request.POST['phone']
        data=request.POST['data']
        time=request.POST['time']
        more_info=request.POST['more_info']
        addresses = UserAddress.objects.create(address=address, city=city,postcode=postcode,phone=phone,data=data,hour=time,more_info=more_info)
        request.session['Address_id'] = addresses.id
        return redirect('form6/')

class EditView(View):
    def get(self, request):

        return render(request, 'form6.html',)

    def post(self, request):
        type = request.POST['products']
        gift = Gifts.objects.create(type=type)
        request.session['Product_id'] = gift.id
        return redirect('form/')

def my_view(request):
    msg=""
    username = request.POST['nick']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        msg="Brak użytkownika w bazie"
    return render(request,'index.html',{'msg':msg})

def logout_view(request):
    logout(request)