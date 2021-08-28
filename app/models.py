from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class User(AbstractUser):
    user_type_data=(("Seller","Seller"),("Customer","Customer"))
    user_type=models.CharField(choices=user_type_data,max_length=10)

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.user_type = "Seller"
        else:
            self.user_type = "Customer"
        super(User, self).save(*args, **kwargs)


class Book(models.Model):
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField() 

    def __str__(self):
        return str(self.bookname)+"["+str(self.price)+']'


class PurchaseBook(models.Model):
    customername = models.CharField(max_length=50)
    address = models.TextField()
    bookname = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.customername)+"["+str(self.book)+']'


class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    desc = models.TextField()
    
    def __str__(self):
        return str(self.fname)
