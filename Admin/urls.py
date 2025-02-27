from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
    path('district/',views.district,name='district'),
    path('deldis/<int:id>',views.deldis,name='deldis'),
    path('category/',views.category,name='category'),
    path('delcat/<int:id>',views.delcat,name='delcat'),
    path('adminreg/',views.adminreg,name='adminreg'),
    path('deladmin/<int:id>',views.deladmin,name='deladmin'),
    path('place/',views.place,name='place'),
    path('brand/',views.brand,name='brand'),
    path('delbrd/<int:id>',views.delbrd,name='delbrd'),
    path('editdis/<int:id>',views.editdis,name='editdis'),
    path('delplace/<int:id>',views.delplace,name='delplace'),
    path('subcat/',views.subcat,name='subcat'),
    path('delsubcat/<int:id>',views.delsubcat,name='delsubcat'),




   path('HomePage/',views.HomePage,name='HomePage'),
  
   path('acceptdesigner/<int:id>',views.acceptdesigner,name="acceptdesigner"),
   path('rejectdesigner/<int:id>',views.rejectdesigner,name="rejectdesigner"),
 
   path('viewdesigner/',views.viewdesigner,name='viewdesigner'),
   path('viewshop/',views.viewshop,name='viewshop'),
   path('acceptshop/<int:id>',views.acceptshop,name="acceptshop"),
   path('rejectshop/<int:id>',views.rejectshop,name="rejectshop"),
]