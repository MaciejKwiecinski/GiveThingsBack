from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Gifts,UserAddress
# Create your views here.
@login_required
def main(request):
    return render(request,'index.html')

class Gifts(LoginRequiredMixin,View):
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

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})