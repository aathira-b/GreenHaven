from django.shortcuts import render, redirect
from Shop.models import*
from Guest.models import *
from User.models import *
# Create your views here.

def Homepage(request):
    return render(request,'Shop/Homepage.html')

def Myprofile(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    return render(request,'Shop/Myprofile.html',{'shop':shop})

def Editprofile(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    #  print(user.user_name)
    if request.method=="POST":
        shop.shop_name=request.POST.get("shop_name")
        shop.shop_email=request.POST.get("shop_email")
        shop.shop_contact=request.POST.get("shop_contact")
        shop.shop_address=request.POST.get("shop_address")
        shop.save()
        return redirect("Shop:Myprofile")
    else:
        return render(request,"Shop/Editprofile.html",{'shop':shop})

# def Changepassword(request):
#     b = tbl_shop.objects.get(id=request.session['sid'])
#     olda = b.shop_password

#     if request.method == "POST":
#         oldb = request.POST.get("shop_old_password")
#         new = request.POST.get("shop_new_password")
#         re = request.POST.get("re_type_password")

#         if olda == oldb:
#             if new == re:
#                 b.shop_password = new
#                 b.save()
#                 return redirect("Shop:Myprofile")
#             return render(request,"Shop/Changepassword.html", {'error': "Your Password doesn't match"})
#         return render(request,"Shop/Changepassword.html", {'error': "Your old password doesn't match"})

def Changepassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_shop.objects.get(id=request.session['sid'])
     olda=b.shop_password
     oldb= new=request.POST.get("shop_old_pasword")
     new=request.POST.get("shop_new_password")
     re=request.POST.get("re_type_password")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.shop_password=request.POST.get("re_type_password")
                b.save()
                return redirect("Shop:Myprofile")
            else:
                return render(request,"Shop/Changepassword.html",{'error1':error1})
        else:
            return render(request,"Shop/Changepassword.html",{'error2':error2})
     else:
         return render(request,"Shop/Changepassword.html")

def addproduct(request):
   category=tbl_category.objects.all()
   pdt=tbl_product.objects.all()
   if request.method=="POST":
      product=request.POST.get("product")
      tbl_product.objects.create(subcategory_id=tbl_subcat.objects.get(id=request.POST.get("sel_subcategory")),product_name=request.POST.get("product_name"),product_details=request.POST.get("product_details"),product_price=request.POST.get("product_price"),product_photo=request.FILES.get("product_photo"),shop=tbl_shop.objects.get(id=request.session["sid"]))
      return render(request,'Shop/Addproduct.html',{'product':pdt,'category':category})
   else:
        return render(request,'Shop/Addproduct.html',{'product':pdt,'category':category})    

def ajaxsubcategory(request):
    sub = tbl_subcat.objects.filter(category=request.GET.get("did"))
    return render(request,"Shop/AjaxSubcategory.html",{"sub":sub})

def viewbooking(request):
    cart = tbl_cart.objects.filter(product__shop=request.session["sid"])
    bkid = []
    for i in cart:
        bkid.append(i.booking.id)
    booking = tbl_booking.objects.filter(id__in=bkid)
    return render(request, "Shop/Viewbooking.html",{"booking":booking})

def delpdt(request,id):
   tbl_product.objects.get(id=id).delete()
   return redirect("Shop:addproduct") 

def stock(request,id):
    pdt=tbl_product.objects.get(id=id)
    stock=tbl_stock.objects.filter(product_id=id)
    if request.method=='POST':
        qty=request.POST.get('Quantity')
        tbl_stock.objects.create(stock_quantity=qty,product_id=pdt)  
        return render(request,'Shop/Addstock.html',{'quantity':stock})
    return render(request,'Shop/Addstock.html',{'quantity':stock})                 