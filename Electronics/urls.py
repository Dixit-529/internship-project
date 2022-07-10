from django.urls import path
from .views import Loginview,Signupview,Homeview ,AboutUsview ,ContectUsview,viewmobile,viewlaptop, viewaccessories ,productdelete , productedit ,Customerlogoutview , Vendorlogoutview



urlpatterns=[
    path('' , Loginview , name='login'),
    path('signup/' , Signupview , name='signup'),
    path('home/' , Homeview , name='Home'),
    path('about/' , AboutUsview , name='About'),
    path('contact/' , ContectUsview , name='Contact'),
    path('mobile/<int:xyz>/' , viewmobile , name='mobile'),
    path('laptop/<int:xyz>/' , viewlaptop , name='laptop'),
    path('accessories/<int:xyz>/' , viewaccessories , name='accessories'),
    path('del/<int:abc>/' , productdelete , name='delete'),
    path('edit/<str:catagory>/<int:abc>/' , productedit , name='Update'),
    path('custmer_logout/' , Customerlogoutview , name='logout as coustmer'),
    # path('Vendor_logout/' , Vendorlogoutview , name='logout as vendor'),
]