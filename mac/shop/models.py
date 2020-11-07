

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from django_countries.fields import CountryField


class Seller(models.Model):
    name = models.CharField(max_length=255, null=True)
    seller_type = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    primary_mob = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    secondary_mob = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) # validators should be a list
    address = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


CATEGORY_CHOICES=(("S","Staples"),("P","Personal Care"),
                  ("H","Household Care"),("P","Packed items"),
                  ("S&B","Snacks & beverage"),)
class Product(models.Model):

    product_name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    made_in= CountryField(multiple=False,default="India")
    image = models.ImageField(upload_to='shop/images', default="")
    image_1 = models.ImageField(upload_to="shop/images", default="Not Available")
    image_2 = models.ImageField(upload_to="shop/images", default="Not Available")

    def __str__(self):
        return self.product_name



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=254)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	primary_mob = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	secondary_mob = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) # validators should be a list

	def __str__(self):
		return self.name



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111, default='Gorakhpur')
    state = models.CharField(max_length=111, default='Uttar Pradesh')
    zip_code = models.IntegerField(default=273003)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    desc = models.TextField()


    def __str__(self):
        return self.name


