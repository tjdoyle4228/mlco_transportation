from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *
from django.db.models import Count 
from django import template

# Create your views here.

def index(request):
    return render(request,'index.html')

def create_user(request):
    if request.method =='POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/entryPage')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def login(request):
    if request.method == 'POST':
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/main/page')
        messages.error(request,"Email or password is wrong")
    return redirect('/login/page')

def entryPage(request):
    if 'user_id' not in request.session:
        return redirect('/') 
    context = {
        'current_user' : User.objects.get(id=request.session['user_id']),
    }
    return render(request,"invoice_entry.html",context)

def login(request):
    if request.method == 'POST':
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/entryPage')
        messages.error(request,"Email or password is wrong")
    return redirect('/')

def log_invoice(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        invoice = Transportation_Invoice.objects.create(
            invoice_number=request.POST['invoice_number'],
            control_date=request.POST['control_date'],
            route_id=request.POST['route_id'],
            miles=request.POST['miles'],
            milage_charge = request.POST['miles_charge'],
            flat_rate = request.POST['flat_date'],
            tractor_fuel_charge = request.POST['tractor_fuel_charge'],
            trailer_fuel_charge = request.POST['trailer_fuel_charge'],
            layover_charge = request.POST['layover_charge'],
            yard_charge = request.POST['yard_charge'],
            toll_charge = request.POST['miles'],
            detention_charge = request.POST['detention_charge'],
            holiday_charge = request.POST['holiday_charge'],
            misc_charge = request.POST['miles'],
            stop_charge = request.POST['miles'],
            stop_count = request.POST['stop_count'],
            unload_hours = request.POST['unload_hours'],
            backhaul_credit = request.POST['backhaul_credit'],
            invoice_entered_by = User.objects.get(id=request.session['user_id']),
            venodor = request.POST['vendor'])
        return redirect('/entryPage')


def add_vendor(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        vendor = Vendor.objects.create(
            vendor_id=request.POST['vendor_id'],
            vendor_name=request.POST['vendor_name'],
            vendor_type=request.POST['vendor_type'],)
        return redirect('/addVendor')

def invoice_data(request):
    if 'user_id' not in request.session:
        return redirect('/') 
    context = {
        'current_user' : User.objects.get(id=request.session['user_id']),
        'invoices' : Transportation_Invoice.objects.all()
    }
    return render(request,"invoice_data.html",context)

def add_vendor_page(request):
    if 'user_id' not in request.session:
        return redirect('/') 
    context = {
        'current_user' : User.objects.get(id=request.session['user_id']),
    }
    return render(request,"add_vendor.html",context)

