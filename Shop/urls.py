from django.urls import path
from Shop import views
app_name="Shop"
urlpatterns=[
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('delpdt/<int:id>',views.delpdt,name='delpdt'),
    path('stock/<int:id>',views.stock,name='stock'),
]