from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.


def district(request):
   dis=tbl_district.objects.all()
   if request.method=="POST":
      district=request.POST.get("district")
      tbl_district.objects.create(district_name=district)
      return render(request,'Admin/District.html',{'district':dis})
   else:
        return render(request,'Admin/District.html',{'district':dis})

def deldis(request,id):
   tbl_district.objects.get(id=id).delete()
   return redirect("Admin:district")           

def category(request):
   cat=tbl_category.objects.all()
   if request.method=="POST":
      category=request.POST.get("category")
      tbl_category.objects.create(category_name=category)
      return render(request,'Admin/Category.html',{'category':cat})
   else:
        return render(request,'Admin/Category.html',{'category':cat}) 

def delcat(request,id):
   tbl_category.objects.get(id=id).delete()
   return redirect("Admin:category")                

def adminreg(request):
   admin=tbl_adminreg.objects.all()
   if request.method=="POST":
      name=request.POST.get("name")
      email=request.POST.get("email")
      password=request.POST.get("password")
      tbl_adminreg.objects.create(admin_name=name,admin_email=email,admin_password=password)

      return render(request,'Admin/AdminReg.html',{'result':admin})
   else:
        return render(request,'Admin/AdminReg.html',{'result':admin}) 

def deladmin(request,id):
   tbl_adminreg.objects.get(id=id).delete()
   return redirect("Admin:adminreg")  

def place(request):
   district=tbl_district.objects.all()
   place=tbl_place.objects.all()
   if request.method=="POST":
    dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
    tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
    return redirect("Admin:place")
   else:
    return render(request,'Admin/place.html',{'result':district,'district':place})

def subcat(request):
   category=tbl_category.objects.all()
   subcat=tbl_subcat.objects.all()
   if request.method=="POST":
    cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
    tbl_subcat.objects.create(subcat_name=request.POST.get("txt_subcat"),category=cat)
    return redirect("Admin:subcat")
   else:
    return render(request,'Admin/SubCategory.html',{'result':category,'category':subcat})

def delsubcat(request,id):
   tbl_subcat.objects.get(id=id).delete()
   return redirect("Admin:subcat")
    

def brand(request):
   brd=tbl_brand.objects.all()
   if request.method=="POST":
      brand=request.POST.get("brand")
      tbl_brand.objects.create(brand_name=brand)
      return render(request,'Admin/Brand.html',{'brand':brd})
   else:
      return render(request,'Admin/Brand.html',{'brand':brd})  

def delbrd(request,id):
   tbl_brand.objects.get(id=id).delete()
   return redirect("Admin:brand")    

def editdis(request,id):
   district=tbl_district.objects.get(id=id)
   if request.method=="POST":
      district.district_name=request.POST.get("district")
      district.save()
      return redirect("Admin:district")
   else:   
      return render(request,'Admin/District.html',{'result':district})

def delplace(request,id):
   tbl_place.objects.get(id=id).delete()
   return redirect("Admin:place")   


def HomePage(request):
    return render(request,'Admin/HomePage.html',{'HomePage':HomePage})

def viewdesigner(request):
    pending=tbl_designer.objects.filter(designer_status=0)
    accepted=tbl_designer.objects.filter(designer_status=1)
    rejected=tbl_designer.objects.filter(designer_status=2)
    return render(request,"Admin/Viewdesigner.html",{'pending':pending,'accepted':accepted,'rejected':rejected})


def acceptdesigner(request,id):
    acc=tbl_designer.objects.get(id=id)
    acc.designer_status=1
    acc.save()
    return redirect("Admin:viewdesigner")

def rejectdesigner(request,id):
    rej=tbl_designer.objects.get(id=id)
    rej.designer_status=2
    rej.save()
    return redirect("Admin:viewdesigner")    

def viewshop(request):
    pending=tbl_shop.objects.filter(shop_status=0)
    accepted=tbl_shop.objects.filter(shop_status=1)
    rejected=tbl_shop.objects.filter(shop_status=2)
    return render(request,"Admin/ViewShop.html",{'pending':pending,'accepted':accepted,'rejected':rejected})
           
def acceptshop(request,id):
    acc=tbl_shop.objects.get(id=id)
    acc.shop_status=1
    acc.save()
    return redirect("Admin:viewshop")

def rejectshop(request,id):
    rej=tbl_shop.objects.get(id=id)
    rej.shop_status=2
    rej.save()
    return redirect("Admin:viewshop")  