from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup , Mobiles , Accessories , Laptops
from django.db.models import Q

# Create your views here.
def Loginview(request):
    if request.method=='POST':
        print("123")
        try:
            print("456")
            m = Signup.objects.get(username=request.POST['username'])
            print(m)
            if m.password==request.POST['pass']:
                print("45567")
                request.session['xyz']='m.id'
                return redirect('Home')
                print("234")
                print("dgdf")
            else:
                print("xyz")
                return HttpResponse("wrong password")
        except:
            print("gtr")
            return redirect('signup')
            print("789")
    return render(request , 'login.html')
def Signupview(request):
    if request.method == 'POST':
        model=Signup(request.POST)
        model.username=request.POST['username']
        model.email=request.POST['email']
        model.MobileNo=request.POST['MobileNo']
        model.password=request.POST['pass']
        model.save()
        print("not working")
        return redirect('login')
        print("not saved")
    return render(request , 'signup.html')
def Homeview(request):
    if 'xyz' in request.session.keys():
    # if 9>8:
        try:
            q=request.GET.get('search')
        except:
            q=None
        if q:
            m = Mobiles.objects.filter(Q(brand_name__icontains=q) | Q(name__icontains=q) | Q(price__icontains=q) | Q(Specifications__icontains=q))
            l = Laptops.objects.filter(Q(brand_name__icontains=q) | Q(name__icontains=q) | Q(price__icontains=q) | Q(Specifications__icontains=q))
            a = Accessories.objects.filter(Q(brand_name__icontains=q) | Q(name__icontains=q) | Q(price__icontains=q) | Q(Specifications__icontains=q))
        else:
            m = Mobiles.objects.all()
            a = Accessories.objects.all()
            l = Laptops.objects.all()
        return render(request , 'home.html' , {'M':m , 'A':a , 'L':l}) 

    return redirect('login')
def AboutUsview(request):
    return render(request , 'aboutus.html')
def ContectUsview(request):
    return render(request , 'contact.html')
def viewmobile(request , xyz):
    v=Mobiles.objects.get(id=xyz)
    return render(request,'mobile.html',{'v':v})
def viewlaptop(request , xyz):
    v=Laptops.objects.get(id=xyz)
    return render(request,'laptop.html',{'l':v})
def viewaccessories(request , xyz):
    v=Accessories.objects.get(id=xyz)
    return render(request,'accessories.html',{'a':v})
def productdelete(request,abc):
    dm=Mobiles.objects.get(id=abc)
    dm.delete()
    dl=Laptops.objects.get(id=abc)
    dl.delete()
    da=Accessories.objects.get(id=abc)
    da.delete()
    return redirect('Home')
def productedit(request , abc ,catagory):
    print("5466")
    if 'xyz' in request.session.keys():
        print("465676")
        # print(request.POST['product_name'])
        if catagory=='Mobile':
            print("345")
            model=Mobiles.objects.get(id=abc)
            brand_name=request.POST['brand_name']
            name=request.POST['product_name']
            price=request.POST['price']
            Specifications=request.POST['specification']
            img=request.FILES.get('img')
            review=request.POST['review']

            model.brand_name=brand_name
            model.name=name
            model.price=price
            model.Specifications=Specifications
            model.img=img
            model.review=review
            model.save()
            print("4545")
            return redirect('Home')
    print("54546")
    return render(request , 'edit.html')
            
        