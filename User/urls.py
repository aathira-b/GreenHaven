from django.urls import path
from User import views
app_name="User"
urlpatterns=[
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('Mybooking/',views.Mybooking,name='Mybooking'),
    path('Viewproduct/',views.Viewproduct,name='Viewproduct'),


    path('Addcart/<int:pid>',views.Addcart, name='Addcart'),   
path('Mycart/',views.Mycart, name='Mycart'),   
path("DelCart/<int:did>", views.DelCart,name="delcart"),
path("CartQty/", views.CartQty,name="cartqty"),

path("productpayment/", views.productpayment,name="productpayment"),
path('loader/',views.loader, name='loader'),
path('paymentsuc/',views.paymentsuc, name='paymentsuc'),


]
