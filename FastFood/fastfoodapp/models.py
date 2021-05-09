from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# from __future__ import unicode_literals


# Create your models here.



class Restaurant(models.Model):
    R_Name=models.CharField(max_length=200,unique=True)
    R_Type=models.CharField(max_length=150)
    R_Email=models.EmailField(max_length=200,unique=True)
    R_Phone=models.BigIntegerField(default=0,unique=True)
    R_Password=models.CharField(max_length=200)
    R_City=models.CharField(max_length=200)
    R_Area=models.CharField(max_length=200,default="Qena")
    R_Image = models.ImageField(upload_to='media/media/images', default="null")
    R_Rate= models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    RImage_Cover = models.ImageField(upload_to='media/media/images', default="null")



    class Meta:
        verbose_name_plural = 'Restaurants'
        
    def __str__(self):
        return self.R_Name





class FoodItem(models.Model):
    It_Name = models.CharField(max_length=200)
    It_Kind = models.CharField(max_length=200)
    It_Size = models.CharField(max_length=200)
    It_Prise = models.PositiveIntegerField(default= 0.0)
    It_Descrip = models.CharField(max_length=200, default='null')
    F_Images= models.ImageField(upload_to='media/media', default='null')
    F_Rate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    foods = models.ManyToManyField(Restaurant)




    def __str__(self):
        return self.It_Name
    



# class Add(models.Model): 
#     R_id = models.ForeignKey(Restaurant(), default=1 ,on_delete= models.SET_DEFAULT)
#     F_id=models.ForeignKey(FoodItem(),default=1,on_delete=models.SET_DEFAULT)
    













# class has(models.Model):
#     Food_it_id = models.ForeignKey(FoodItem(),default=1 ,on_delete=models.SET_DEFAULT)
#     Delivery_id= models.ForeignKey(DeliveryInfo(), default=1, on_delete=models.SET_DEFAULT)
    




class Customer(models.Model):
    C_Fname=models.CharField(max_length=200)
    C_Lname=models.CharField(max_length=200)
    C_Email=models.EmailField(max_length=200,unique=True)
    C_Password=models.CharField(max_length=200)
    C_Password2=models.CharField(max_length=200)
    C_Phone=models.CharField(max_length=200,unique=True)
    C_City=models.CharField(max_length=200)
    C_Area=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Customers'
        
    def __str__(self):
        return self.C_Fname







class Order(models.Model):
    D_Name = models.CharField(max_length=200, default='null')
    D_time = models.DateTimeField(auto_now=True)
    D_totalCost = models.DecimalField(max_digits=5, decimal_places=2, default=000)
    restaurants = models.ManyToManyField(Restaurant)
    customers   = models.ManyToManyField(Customer)
    foods       = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.D_Name
    
    

    



# class Order(models.Model):
#     Customer_id = models.ForeignKey(Customer(),default=1,on_delete=models.SET_DEFAULT)
#     Food_it_id = models.ForeignKey(FoodItem(),default=1,on_delete=models.SET_DEFAULT)
    





# class Receive(models.Model):
    # Customer_id = models.ForeignKey(Customer(), default=1,on_delete=models.SET_DEFAULT)
    # Delivery_id = models.ForeignKey(DeliveryInfo(), default=1, on_delete=models.SET_DEFAULT)







# class food(models.Model):
#     name = models.CharField(max_length=50)


# class vindour(models.Model):
#     Vname = models.CharField(max_length=50)
#     kind  = models.CharField(max_length=50)
#     foods = models.ManyToManyField(food)

    

