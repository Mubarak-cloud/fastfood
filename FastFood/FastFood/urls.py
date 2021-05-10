"""FastFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from fastfoodapp.views import typepage,restaurant_Reg,restaurant,addmeal,delete,Aboutus,loginType,editmeal,yourorders,showorders,editinfo,restaurant_login,customer_reg,customer_login,logout_user
from fastfoodapp.views import mainpage,RestaurantsPage,Rmeal,Outer_SearchBox,Rdessert,OrderPage,index,RestaurantsPage,ordertype,checktype,testview
from fastfoodapp.views import history_of_orders,restaurant_meals


urlpatterns = [
    path('admin/', admin.site.urls),


    # -----------------------------------
    path('',mainpage,name="MainPage"),
    path('restaurant/<int:id>', restaurant_meals, name='restaurant'),




    path('Foods/',Rmeal ,name="Rmeals"),
    path('OrderPage/<int:id>',OrderPage ,name="OrderPage"),
    path('Foods/OrderPage/<int:id>',OrderPage ,name="OrderPage"),
    path('checktype',checktype,name="checktype"),
    path('Restaurants/',Rdessert ,name="RDFPage"),
    path('ordertype',ordertype,name="ordertype"),

    path('Outer_SearchBox/',Outer_SearchBox ,name="search"),
    # path('SearchBox/',SearchBox ,name="SearchBox"),

    path('RestaurantsPage/<int:id>',RestaurantsPage ,name="RestaurantsPage"),
    path('index/<int:id>',index,name="index"),
    path('testview/<int:id>',testview,name="testview"),
    path('RestaurantsPage', testview, name='RestaurantsPage'),
    path('CustomerPage/<int:id>',history_of_orders, name='CustomerPage'),
    path('typepage/',typepage,name="TypePage"),




    # -----------------------------------
    path('restaurantreg',restaurant_Reg,name="RegRestaurant"),
    path('restaurant',restaurant,name="Restaurant"),
    path('restaurant/<int:id>',delete,name="Restaurant"),
    path('restaurant/addmeal',addmeal,name="Addmeal"),
    path('restaurant/editmeal/<int:id>',editmeal,name="Editmeal"), 
    path('yourorders',yourorders,name="Yourorders"),
    path('yourorders/<int:id>',showorders,name="Showorders"),
    path('yourorders/editCustInfo/<int:id>',editinfo,name="EditCustInfo"),
    # path('congratulations',afterReg,name="congratulations"),
    # path('login/',login,name="login"),
    path('loginRes/',restaurant_login,name="loginRes"),
    path('customerlogin/',customer_login,name="customerlogin"),
    path('logout/',logout_user,name="logout"),
    path('about/',Aboutus,name="aboutus"),
    path('customerreg/',customer_reg ,name="customerreg"),
    # path('User/',User ,name="user"),
    # path('User1/',curentuser,name="user1"),
    # path('loginforrestuarnt/',loginRestuarnt ,name="login2"),
    path('loginType/',loginType ,name="loginType"),
    # path('newuser/',newUser ,name="newuser"),
    # path('pass/',forgetpass,name="password"),
    # path('change/',changepass,name="changepassword"),




]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
