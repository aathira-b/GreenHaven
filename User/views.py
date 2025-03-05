from django.shortcuts import render, redirect
from User.models import*
from Guest.models import *
from Shop.models import *
from django.db.models import Sum
# Create your views here.

def Homepage(request):
    if "uid" in request.session:
        return render(request,'User/Homepage.html')
    else:
        return redirect("Guest:Login")

def Myprofile(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session["uid"])
        return render(request,'User/Myprofile.html',{'user':user})
    else:
        return redirect("Guest:Login")

       


def Editprofile(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session["uid"])
        #  print(user.user_name)
        if request.method=="POST":
            user.user_name=request.POST.get("user_name")
            user.user_email=request.POST.get("user_email")
            user.user_contact=request.POST.get("user_contact")
            user.user_address=request.POST.get("user_address")
            user.save()
            return redirect("User:Myprofile")
        else:
            return render(request,"User/Editprofile.html",{'user':user})
    else:
        return redirect("Guest:Login")



def Changepassword(request):
    if "uid" in request.session:
        b = tbl_user.objects.get(id=request.session['uid'])
        olda = b.user_password

        if request.method == "POST":
            oldb = request.POST.get("user_old_pasword")
            new = request.POST.get("user_new_password")
            re = request.POST.get("re_type_password")

            if olda == oldb:
                if new == re:
                    b.user_password = new
                    b.save()
                    return redirect("User:Myprofile")
                return render(request, "User/Changepassword.html", {'error': "Your Password doesn't match"})
            return render(request, "User/Changepassword.html", {'error': "Your old password doesn't match"})
        else:
            return render(request, "User/Changepassword.html")
    else:
        return redirect("Guest:Login")




def Feedback(request):
    if "uid" in request.session:
        msg=tbl_feedback.objects.all()
        if request.method=="POST":
            data=request.POST.get('feedback')       
            tbl_feedback.objects.create(feedback_content=data)
            return render(request,'User/Feedback.html',{'feedback':msg})
        else:
            return render(request,'User/Feedback.html',{'feedback':msg})
    else:
        return redirect("Guest:Login")




def Viewproduct(request):
    if "uid" in request.session:
            pro=tbl_product.objects.all()
            return render(request,'User/Viewproduct.html',{'product':pro})
    else:
        return redirect("Guest:Login")



def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/Viewproduct.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/Viewproduct.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/Viewproduct.html",{'msg':msg})

def Mycart(request):
    if "uid" in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_totalamount=request.POST.get("carttotalamt")
            bookingdata.booking_adv_amount=float(request.POST.get("carttotalamt"))*10
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_stock = tbl_stock.objects.filter(product_id=i.product.id).aggregate(total=Sum('stock_quantity'))['total']
                    total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=0).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")
    else:
        return redirect("Guest:LoginForm")
        

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:Mycart")   

def productpayment(request):
    bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
    amt = bookingdata.booking_adv_amount
    
    if request.method == "POST":
        bookingdata.booking_status = 2
        bookingdata.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amt":amt})
    

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")


def Mybooking(request):
    if "uid" in request.session:
        booking=tbl_booking.objects.filter(booking_status__gt=0,user=request.session['uid'])   
        return render(request,'User/Mybooking.html',{'result':booking})     
    else:
         return redirect("Guest:Login")    