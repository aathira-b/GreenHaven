from django.shortcuts import render, redirect
from Admin.models import *
from Guest.models import *

# Create your views here.
def login(request):
    return render(request,'Guest/Login.html')

def Registration(request):
    dis=tbl_district.objects.all()
    return render(request,'Guest/Registration.html',{'result':dis,})

def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})    

def Registration(request):
    dis=tbl_district.objects.all()
    # a=tbl_reg.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_user.objects.create(user_name=request.POST.get("user_name"),user_email=request.POST.get("user_email"),user_contact=request.POST.get("user_contact"),user_password=request.POST.get("user_password"),user_address=request.POST.get("user_address"),user_photo=request.FILES.get("file_photo"),place=place)
        return redirect("Guest:Registration")
    else:
        return render(request,'Guest/Registration.html',{'result':dis})


def login(request):
    if request.method=="POST":
        email=(request.POST.get("email"))
        password=(request.POST.get("password"))
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        designercount=tbl_designer.objects.filter(designer_email=email,designer_password=password).count()
        shopcount=tbl_shop.objects.filter(shop_email=email,shop_password=password).count()
        if usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)   
            request.session["uid"]=user.id
            return redirect("User:Homepage")
        elif designercount>0:
            designer=tbl_designer.objects.get(designer_email=email,designer_password=password)   
            request.session["eid"]=designer.id
            return redirect("Designer:HomePage")  
        elif admincount>0:
            admin=tbl_adminreg.objects.get(admin_email=email,admin_password=password)   
            request.session["aid"]=admin.id
            return redirect("Admin:HomePage")  
        elif shopcount>0:
            shop=tbl_shop.objects.get(shop_email=email,shop_password=password)   
            request.session["sid"]=shop.id
            return redirect("Shop:Homepage")       

        else:
            return render(request,'Guest/Login.html')    
    else:
            return render(request,'Guest/Login.html')    

def Designer(request):
    dis=tbl_district.objects.all()
    # a=tbl_reg.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_designer.objects.create(designer_name=request.POST.get("designer_name"),designer_email=request.POST.get("designer_email"),designer_contact=request.POST.get("designer_contact"),designer_address=request.POST.get("designer_address"),designer_password=request.POST.get("designer_password"),designer_photo=request.FILES.get("file_photo"),designer_proof=request.FILES.get("file_proof"),place=place)
        return redirect("Guest:Designer")
    else:
        return render(request,'Guest/Designer.html',{'result':dis})            

def Shop(request):
    dis=tbl_district.objects.all()
    # a=tbl_reg.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_shop.objects.create(shop_name=request.POST.get("shop_name"),shop_email=request.POST.get("shop_email"),shop_contact=request.POST.get("shop_contact"),shop_address=request.POST.get("shop_address"),shop_password=request.POST.get("shop_password"),shop_logo=request.FILES.get("file_photo"),shop_license=request.FILES.get("file_proof"),place=place)
        return redirect("Guest:Shop")
    else:
        return render(request,'Guest/Shop.html',{'result':dis})                    