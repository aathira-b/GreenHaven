from django.shortcuts import render, redirect
from Designer.models import*
from Guest.models import *
# Create your views here.

def HomePage(request):
    return render(request,'Designer/HomePage.html',{'HomePage':HomePage})

def Myprofile(request):
    designer=tbl_designer.objects.get(id=request.session["eid"])
    return render(request,'Designer/Myprofile.html',{'designer':designer})

def Editprofile(request):
     b=tbl_designer.objects.get(id=request.session["eid"])
     if request.method=="POST":
        b.designer_name=request.POST.get("designer_name")
        b.designer_email=request.POST.get("designer_email")
        b.designer_contact=request.POST.get("designer_contact")
        b.designer_address=request.POST.get("designer_address")
        b.save()
        return redirect("Designer:Myprofile")
     else:
         return render(request,"Designer/Editprofile.html",{'designer':b})

def Changepassword(request):
    b = tbl_designer.objects.get(id=request.session['eid'])
    olda = b.designer_password

    if request.method == "POST":
        oldb = request.POST.get("designer_old_pasword")
        new = request.POST.get("designer_new_password")
        re = request.POST.get("re_type_password")

        if olda == oldb:
            if new == re:
                b.designer_password = new
                b.save()
                return redirect("Designer:Myprofile")
            return render(request, "Designer/Changepassword.html", {'error': "Your Password doesn't match"})
        return render(request, "Designer/Changepassword.html", {'error': "Your old password doesn't match"})
    
    return render(request, "Designer/Changepassword.html")

def Work(request):
    work=tbl_work.objects.all()
    if request.method=="POST":
        tbl_work.objects.create(work_name=request.POST.get("work_name"),work_photo=request.FILES.get("work_photo"),work_details=request.POST.get("work_details"))
        return render(request,'Designer/Work.html',{'work':work}) 
    else:
        return render(request,'Designer/Work.html',{'work':work})    

def delwork(request,id):
    tbl_work.objects.get(id=id).delete()
    return redirect("Designer:Work") 

def Gallery(request):
    gallery=tbl_gallery.objects.all()
    if request.method=="POST":
        tbl_gallery.objects.create(gallery_photo=request.FILES.get("gallery_photo"),designer_id=tbl_designer.objects.get(id=request.session['eid']))
        return render(request,'Designer/Gallery.html') 
    else:
        return render(request,'Designer/Gallery.html',{'gallery': gallery})    

def delgallery(request,id):
    tbl_gallery.objects.get(id=id).delete()
    return redirect("Designer:Work") 
