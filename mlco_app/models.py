from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self,form):
        errors = {}
        if len(form['first_name']) <2:
            errors['first_name'] = 'First name needs to be at least 2 characters long'
        if len(form['last_name']) <2:
            errors['last_name'] = 'Last name needs to be at least 2 characters long'        
        if len(form['password']) < 6:
            errors['password']= 'Password needs to be at least 6 characters long'
        if form['password'] != form['confirm_password']:
            errors['match'] = 'password and pw confirmation do not match'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['regex'] = 'email in wrong format'
        users_with_email = User.objects.filter(email=form['email'])
        if len(users_with_email) >=1:
            errors['dup'] = 'email already taken'
        return errors 

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Vendor(models.Model):
    vendor_id = models.TextField()
    vendor_name = models.TextField()
    vendor_type = models.TextField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transportation_Invoice(models.Model):
    invoice_number = models.TextField()
    control_date = models.DateTimeField()
    route_id = models.TextField()
    miles = models.IntegerField()
    milage_charge = models.DecimalField(max_digits=10, decimal_places=2)
    flat_rate = models.DecimalField(max_digits=10, decimal_places=2)
    tractor_fuel_charge = models.DecimalField(max_digits=10, decimal_places=2)
    trailer_fuel_charge = models.DecimalField(max_digits=10, decimal_places=2)
    layover_charge = models.DecimalField(max_digits=10, decimal_places=2)
    yard_charge = models.DecimalField(max_digits=10, decimal_places=2)
    toll_charge = models.DecimalField(max_digits=10, decimal_places=2)
    detention_charge = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_charge = models.DecimalField(max_digits=10, decimal_places=2)
    misc_charge = models.DecimalField(max_digits=10, decimal_places=2)
    stop_charge = models.DecimalField(max_digits=10, decimal_places=2)
    stop_count = models.IntegerField()
    unload_hours = models.DecimalField(max_digits=10, decimal_places=2)
    backhaul_credit = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_entered_by = models.ForeignKey(User,related_name = 'entered_by',on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,related_name = 'invoice_sender',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Route(models.Model):
    route_id = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    cube = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







