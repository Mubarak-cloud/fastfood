from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
# from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# # from __future__ import unicode_literals


# # Create your models here.


class Restaurant(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # R_Name=models.CharField(max_length=200,unique=True)
    R_Type=models.CharField(max_length=150)
    # R_Email=models.EmailField(max_length=200,unique=True , default='null')
    R_Phone=models.BigIntegerField(default=0,unique=True)
    # R_Password=models.CharField(max_length=200)
    R_City=models.CharField(max_length=200)
    R_Area=models.CharField(max_length=200,default="Qena")
    R_Image = models.ImageField(upload_to='media/media/media/media', default="null")
    R_Rate= models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    RImage_Cover = models.ImageField(upload_to='media/images', default="null")
    
    class Meta:
             verbose_name_plural = 'Restaurants'
        
    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,unique=True)
    City=models.CharField(max_length=20)
    Area=models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Customers'
        
    def __str__(self):
        return self.user.username


# class Restaurant(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE,default='null')
#     # R_Name=models.CharField(max_length=200,unique=True)
#     R_Type=models.CharField(max_length=150)
#     # R_Email=models.EmailField(max_length=200,unique=True)
#     R_Phone=models.BigIntegerField(default=0,unique=True)
#     # R_Password=models.CharField(max_length=200)
#     R_City=models.CharField(max_length=200)
#     R_Area=models.CharField(max_length=200,default="Qena")
#     R_Image = models.ImageField(upload_to='media/images', default="null")
#     R_Rate= models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
#     RImage_Cover = models.ImageField(upload_to='media/images', default="null")



#     class Meta:
#         verbose_name_plural = 'Restaurants'
        
#     def __str__(self):
#         return self.user.username


class FoodItem(models.Model):
    It_Name = models.CharField(max_length=200)
    It_Kind = models.CharField(max_length=200)
    It_Size = models.CharField(max_length=200)
    It_Prise = models.IntegerField(default= 0, null=True)
    It_Descrip = models.CharField(max_length=200, default='null')
    F_Images= models.ImageField(upload_to='media/media/media/media', default='null')
    F_Rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    foods = models.ManyToManyField(Restaurant)




    def __str__(self):
        return self.It_Name
    




class Order(models.Model):
    D_Name = models.CharField(max_length=200, default='null')
    D_time = models.DateTimeField(auto_now=True)
    D_totalCost = models.DecimalField(max_digits=5, decimal_places=2, default=000)
    restaurants = models.ManyToManyField(Restaurant)
    customers   = models.ManyToManyField(Customer)
    foods       = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.D_Name



class Addtocard(models.Model):
    name = models.CharField(max_length=200, default='null')
    kind = models.CharField(max_length=200, default='null')
    size = models.CharField(max_length=200, default='null')
    prise = models.IntegerField(default= 0, null=True)
    descrip = models.CharField(max_length=200, default='null')
    images= models.ImageField(upload_to='media/media/media/media', default='null')
    
    
    
    

    

