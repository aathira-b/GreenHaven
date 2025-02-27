from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('login/',views.login,name='Login'),
    path('Registration/',views.Registration,name='Registration'),
    path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
    path('Designer/',views.Designer,name='Designer'),
    path('Shop/',views.Shop,name='Shop'),

]