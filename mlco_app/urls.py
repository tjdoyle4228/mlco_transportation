from django.urls import path
from . import views



urlpatterns  = [
    path('',views.index),
    path('users/create',views.create_user),
    path('logout',views.logout),
    path('users/login',views.login),
    path('entryPage',views.entryPage),
    path('login',views.login),
    path('invoiceData',views.invoice_data),
    path('addVendorPage',views.add_vendor_page),
    path('addVendor',views.add_vendor),
    
    



]