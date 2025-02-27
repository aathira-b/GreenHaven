from django.urls import path
from Designer import views
app_name="Designer"
urlpatterns=[
    path('HomePage/',views.HomePage,name='HomePage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('Work/',views.Work,name='Work'),
    path('delwork/<int:id>',views.delwork,name='delwork'),
    path('Gallery/',views.Gallery,name='Gallery'),
    path('delgallery/<int:id>',views.delgallery,name='delgallery'),
]