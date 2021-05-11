from django.shortcuts import render,HttpResponse,redirect
# from . import models
import re
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from .models import Restaurant,FoodItem,Customer,Order
from .models import *




# Create your views here.



        #       Mubarak Functions workplace        #

    # Main page functions
def mainpage(request):
    Restobject = Restaurant.objects.all()
    Foods = FoodItem.objects.all()
    
    return render(request,'Mubarak html files/mainPage.html',{
        'Restobject': Restobject[0:3],'Foods':Foods}
         )

    # Restaurant page functions 
@login_required(login_url='loginRes')
def restaurant_meals(request, id):
        #  globale variables for if condtions
    restaurant_meals = None
    customers_orders = None
    recive_orders    = None
    food_item        = None
        #  to show current Restaurant data
    Restaurant_id = Restaurant.objects.get(id=id)
    if Restaurant_id :
            #  to show restaurant meals
        restaurant_meals = FoodItem.objects.filter(foods__id=id)
        # print(restaurant_meals)

            # to show customers orders 
        customers_orders = Order.objects.all().filter(restaurants__id =id)
        # print('customer orders variable -----')
        print(customers_orders)
        if customers_orders:
            recive_orders = customers_orders
            # print('recive orders variabel ----')
            # print(recive_orders)
        else:
            recive_orders = 'thers is no orders for today'
            # print(recive_orders)


            #  to add new meal 
        if request.method == "POST":
            meal_name = request.POST.get('name')
            meal_kind = request.POST.get('Kind')
            meal_size = request.POST.get('Size')
            meal_prise= request.POST.get('Price')
            meal_Descr= request.POST.get('Description')
            meal_rate = request.POST.get('Rate')
            meal_image= request.POST.get('Image')

            food_item = FoodItem(

                It_Name   = meal_name,
                It_Kind   = meal_kind,
                It_Size   = meal_size,
                It_Prise  = meal_prise,
                It_Descrip= meal_Descr,
                F_Rate    = meal_rate,
                F_Images  = meal_image

            )
            food_item.save()
            food_item.foods.add(Restaurant_id)
            # print('food item variable')
            # print(food_item)
            
        #     return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {})
        # else:
        #     return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {})
    return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {
        #  to show current Restaurant data
        'R_id'      : Restaurant_id.id,
        'R_Image'   : Restaurant_id.R_Image,
        'user.username'    : Restaurant_id.user.username,
        'R_Type'    : Restaurant_id.R_Type,
        'user.email'   : Restaurant_id.user.email,
        'R_Phone'   : Restaurant_id.R_Phone,
        'R_Rate'    : Restaurant_id.R_Rate,
        'R_City'    : Restaurant_id.R_City,
        'R_Area'    : Restaurant_id.R_Area,
        'RImage_Cover': Restaurant_id.RImage_Cover,

        #  to show restaurant meals
        'restaurant_meals' : restaurant_meals,

        #  to show today orders 
        'recive_orders'     : recive_orders,

        # to add new meal 

    })
    


            
#   function for restauratns --- this function do the exact thing like above and i did that to handle old version pages " Restaurant page "
def RestaurantsPage(request, id ):
        #  globale variables for if condtions
    restaurant_meals = None
    customers_orders = None
    recive_orders    = None
    food_item        = None

        #  to show current Restaurant data
    Restaurant_id = Restaurant.objects.get(id=id)
        #  to show restaurant meals
    restaurant_meals = FoodItem.objects.filter(foods__id=id)
    # print(restaurant_meals)

            # to show customers orders 
    customers_orders = Order.objects.all().filter(restaurants__id =id)
    print(customers_orders)
    if customers_orders:
        recive_orders = customers_orders
        print(recive_orders)
    else:
        recive_orders = 'thers is no orders for today'
        # print(recive_orders)


        #  to add new meal 
    if request.method == "POST":
        meal_name = request.POST.get('name')
        meal_kind = request.POST.get('Kind')
        meal_size = request.POST.get('Size')
        meal_prise= request.POST.get('Prise')
        meal_Descr= request.POST.get('Description')
        meal_rate = request.POST.get('Rate')
        meal_image= request.POST.get('Image')

        food_item = FoodItem(

            It_Name   = meal_name,
            It_Kind   = meal_kind,
            It_Size   = meal_size,
            It_Prise  = meal_prise,
            It_Descrip= meal_Descr,
            F_Rate    = meal_rate,
            F_Images  = meal_image

        )
        food_item.save()
        food_item.foods.add(Restaurant_id)
        


    return render(request, 'Mubarak html files/ManyToMany/restForCustomer.html', {
        #  to show current Restaurant data
        'R_id'      : Restaurant_id.id,
        'R_Image'   : Restaurant_id.R_Image,
        'user.username'    : Restaurant_id.user.username,
        'R_Type'    : Restaurant_id.R_Type,
        'user.email'   : Restaurant_id.user.email,
        'R_Phone'   : Restaurant_id.R_Phone,
        'R_Rate'    : Restaurant_id.R_Rate,
        'R_City'    : Restaurant_id.R_City,
        'R_Area'    : Restaurant_id.R_Area,
        'RImage_Cover': Restaurant_id.RImage_Cover,

                #  to shoe restaurant meals
        'restaurant_meals' : restaurant_meals,

                #  to show today orders 
        'recive_orders'     : recive_orders

    })




                    # customers functions here 
                

        # to show previous orders
@login_required(login_url='customerlogin')
def history_of_orders(request, id):
        #  global variables for if condations 
    customerinfo = None
    history  = None
    message  = None
    checkuesr= None

        #  get and check the user 
    checkuesr = Customer.objects.get(id=id)
    print(checkuesr.phone)
    if checkuesr:
        # customerinfo = Customer.objects.get(id=id)
        history= Order.objects.all().filter(customers__id=id)
        message = 'ther is no orders'

        # if request.method == 'POST':
        #     A_1 = request.POST
        customer_First_Name = request.POST.get('FName'),
        #     customer_Last_Name  = request.POST.get('LName'),
        #     customer_Email      = request.POST.get('email'),
        #     customer_password   = request.POST.get('Password'),
        #     customer_password_2 = request.POST.get('Password2'),
        customer_Phone      = request.POST.get('Phone'),
        customer_City       = request.POST.get('City'), 
        customer_Area       = request.POST.get('Area')

        # checkuesr.objects.update(
        #     user = customer_First_Name,
        #     phone= customer_Phone,
        #     City = customer_City,
        #     Area = customer_Area
        # )
    


    

    return render(request, 'Mubarak html files/ManyToMany/customersOrders.html', {
        # 'customerinfo': customerinfo,
        'history' : history,
        'message' : message,
        'checkuesr': checkuesr
    })


def addtocard(request,cust_id,meal_id):
    customerObj = Customer.objects.get(id=cust_id)
    oederObj = FoodItem.objects.get(id=meal_id)
    print(oederObj.It_Name,customerObj.C_Fname)

    myorder=Addtocard.objects.create(
        Customer_id=customerObj,
        Food_it_id=oederObj
        )

    return render(request,'Mubarak html files/mainPage.html',{})


def details(request):
    foods_orders = Addtocard.objects.all()
    return render(request,'details.html',{'foods_orders' : foods_orders})





    # Food Page function 

def Rdessert(request):
    dessert = Restaurant.objects.all()
    # print("hi")
    # for d in dessert:
    #     print("hello")
    #     print(d)
    return render(request,'Mubarak html files/Restaurnts.html',{
        'dessert' : dessert
        })



def Rmeal(request):
    meals = FoodItem.objects.all()
    # print(meals)
    return render(request, 'Mubarak html files/Foods.html', {
        'meals':meals,
        })



        # Search Fuchtion 
# def SearchBox(request):
#     print("hi")
#     if request.method == "GET":
#         searched = request.GET.get('searched')
#         FList = FoodItem.objects.all().filter(It_Name__iexact=searched)
#         Flist_Two = FoodItem.objects.all().filter(It_Name__startwith=searched[0])
#         print(searched)
#         return render(request, 'Mubarak html files/test.html', {
#             'searched':searched,
#              'FList' : FList,
#              'Flist_two': Flist_Two,
#             })
#     else:
#         return render(request, 'Mubarak html files/test.html', {})


# @csrf_exempt
def Outer_SearchBox(request):
    if request.method == "POST":
        outer_search = request.POST.get('searched')
        #line270 change from R_Name to R_Phone
        Rlist = Restaurant.objects.all().filter(R_Phone__iexact=outer_search)
        Rlist_two = Restaurant.objects.all().filter(R_Phone__istartswith=outer_search[0])

        Flist_two= FoodItem.objects.all().filter(It_Name__iexact=outer_search)
        Flist_Three = FoodItem.objects.all().filter(It_Name__istartswith=outer_search[0])
        # print(Flist_Three)
        return render(request, 'Mubarak html files/test.html', {
            'outer_search': outer_search,
            'Flist_two':Flist_two,
            'Flist_Three' : Flist_Three ,
            'Rlist'       : Rlist,
            'Rlist_two'   : Rlist_two, 
            })
    else:
        return render(request, 'Mubarak html files/test.html', {})


def index(request, id):
    # itemId = testModel.objects.all()
    tesItem= testModel.objects.get(Mid=id)
    # print(tesItem)
    return render(request, 'Mubarak html files/base.html', {
        # 'item': item.It_Name,
        # 'itemId': itemId,
        'tesItem': tesItem.MName ,
          
    })


def OrderPage(request, id):
        # global variables for if condetions
    orders = None

    current_user = request.user
    order = FoodItem.objects.get(id=id)
    # B = Restaurant.objects.all()
    print(current_user)
    # print(order.foods)
    if order:
        # print(order)
        if request.method == "POST":
            # print(order)
            orders = Order(
                D_Name = order.It_Name,
                D_totalCost = order.It_Prise,
            )
            orders.save()
            # print(orders)
            orders.customers.add(current_user)
            # A = Customer.objects.all()
            # orders.restaurants.add(B[0].id)

            # orders.restaurants.set(order.foods)
            # orders.restaurants.add()
            # print(orders)

    return render(request, 'Mubarak html files/OrdersPage.html', {
        'order': order,
        'orderName': order.It_Name,
        'orderKink': order.It_Kind,
        'orderSize': order.It_Prise,
        'orderDescription': order.It_Descrip,
        'orderImages': order.F_Images,
        'orderRate': order.F_Rate
    })





def ordertype(request):
    if request.method == "POST":
        return render(request, 'Mubarak html files/ordertype.html', {})
    if request.method == "GET":
        return render(request, 'Mubarak html files/ordertype.html', {})
    


def checktype(request):
    if request.method == "GET":
        getEmail = request.GET.get('Email')
        getPass  = request.GET.get('password')
        try:
            checkEmail = Customer.objects.get(C_Email=getEmail)
            checkpass  = Customer.objects.get(C_Password=getPass)

            return render(request, 'Mubarak html files/checkResult.html', {
                'rightEmail': checkEmail,
                'rightPassword' : checkpass,
            })

        except models.Customer.DoesNotExist:
            return render(request, 'Mubarak html files/checkResult.html', {
                'WrongINput': 'Wrong INput',
            }) 
    else:
        return render(request, 'Mubarak html files/checkResult.html', {})  


    











def testview(request, id):
    restid = Restaurant.objects.get(id=id)
    # foods = FoodItem.objects.all().get(It_Name='F1')
    if request.method == "POST":
        fname = request.POST['name']

        cobj = FoodItem.objects.create(
            It_Name= fname,
        )
        cobj.save()
        cobj.foods.add(restid)
        A = FoodItem.objects.all().filter(foods__id=id)
        # print(A)
    return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {
        'A' : A ,
    })












              # mubarak workespace end here 
        # --------------------------------------------------#



def typepage(request):
    return render(request,'typePage.html',{})

def restaurant_Reg(request):
    if request.method == "POST":
        cd = request.POST
        if get_user_model().objects.filter(email=cd['email']) or get_user_model().objects.filter(username=cd['full_name']):
            messages.warning(request, 'email or name used before')
            return redirect('register')
        obj = Restaurant()
        obj.user = get_user_model().objects.create_user(username=cd['full_name'])
        obj.user.email = cd['email']
        obj.user.set_password(cd['password'])
        obj.user.save()
        obj.R_Phone = cd['phone']
        obj.R_Type = cd['restype']
        obj.R_Area = cd.get("area")
        obj.R_City = cd.get("city")
        obj.save()
        messages.success(request, 'registeration is successfully')
        return redirect('loginRes')
    return render(request,'regestrationforrestuarnt.html',{})

def restaurant_login(request):
    
    cd = request.POST

    if request.method == "POST":
        user = authenticate(request, username=get_user_model().objects.filter(email=cd['email'])[0].username, password=cd['password'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'invalid email or password')
            return redirect('loginRes')
    
    return render(request,'loginForRestuarant.html',{})


def details(request):
    return render(request,'details.html',{})

def customer(request):
    return render(request,'customer.html',{})

def yourorders(request):
    return render(request,'yourorders.html',{})

def showorders(request,id):
    oederObj = FoodItem.objects.get(id=id)
    return render(request,'yourorders.html',{'oederObj' : oederObj})


def editinfo(request,id):
    customerObj = Customer.objects.get(id=id)
    if request.method == 'POST':
        cust_email=request.POST['cust_email']
        cust_pass=request.POST['cust_pass']
        cust_phone=request.POST['cust_phone']
        
        cust = Customer.objects.filter(id=customerObj.id).update(
            C_Email = cust_email,
            C_Password = cust_pass,
            C_Phone = cust_phone
        )

    return render(request,'editCustInfo.html',{'customerObj' : customerObj})

@login_required(login_url="loginRes")
def restaurant(request):
#DELETD FROM DATABASE
    
 #RETRIVE FROM DATABASE
    foods_details = FoodItem.objects.all()
#    foods_list=[]
 #   for meal in foods_details:
  #      foods_list.append(meal.It_Name)
   #     foods_list.append(meal.It_Size)
    #    foods_list.append(meal.It_Kind)
    
    #print(foods_list)

    return render(request,'restaurant.html',{'foods_details' : foods_details})

def addmeal(request):
    #ADD TO DATABASE
    if request.method == 'POST':
        item_name = request.POST['item_name']
        item_size = request.POST['item_size']
        item_kind = request.POST['item_kind']
        item_prise = request.POST['item_prise']
        item_descrip = request.POST['item_descrip']
        F_Images  = request.POST['item_Image']

        foods = FoodItem.objects.create(
            It_Name = item_name,
            It_Size = item_size,
            It_Kind = item_kind,
            It_Prise = item_prise,
            It_Descrip = item_descrip,
            F_Images= F_Images
        )
    return render(request,'addmeal.html',{})

def editmeal(request,id):
    obj = FoodItem.objects.get(id=id)
  
    if request.method == 'POST':
        it_name = request.POST['it_name']
        it_size = request.POST['it_size']
        it_kind = request.POST['it_kind']
        it_prise = request.POST['it_prise']
        it_descrip = request.POST['it_descrip']

        foods = FoodItem.objects.filter(id=obj.id).update(
            It_Name = it_name,
            It_Size = it_size,
            It_Kind = it_kind,
           It_Prise = it_prise,
           It_Descrip = it_descrip
        )
    return render(request,'editmeal.html',{'obj' : obj})

@login_required(login_url='loginRes')
def delete(request,id):
    obj = FoodItem.objects.get(id=id)
    obj.delete()
    return redirect('/restaurant')


# def afterReg(request):
#     res_name=request.POST['restname']
#     res_type=request.POST['restype']
#     res_email=request.POST['email']
#     res_password=request.POST['pass']
#     res_phone=request.POST['phone']
#     res_city=request.POST['city']
#     res_area=request.POST['area']
#        # error_message=None
#     # if not res_name:
#     #     error_message="Restuarant Name Is Required"
#     # elif len(res_name)<2:
#     #         error_message="Restuarant Name must be 2 char or more "

#     # elif res_type:
#     #     error_message="Restuarant Type Is Required"
#     # elif not res_email:
#     #     error_message=" Email Is Required"
#     # elif not res_password:
#     #     error_message="Password Is Required"
#     # elif not res_phone:
#     #     error_message="Phone Is Required"
#     # elif not res_city:
#     #     error_message="City Is Required"
#     # elif not res_area:
#     #     error_message="Area Is Required"
#     regphone=re.match(r"01(0|1|2|5)[0-9]{8}",res_phone)
#     regpass=re.match(r"^[a-z0-9]{6,20}$",res_password)
#     if regphone and regpass:
#         reg=models.Restaurant(user.username=res_name,R_Type=res_type,user.email=res_email,R_Password=res_password,
#                 R_Phone=res_phone,R_City=res_city,R_Area=res_area)
#         reg.save()
#         messages.info(request,"Successfully Registered")
#         return render(request,"regestrationforrestuarnt.html")
#         # return HttpResponse("Successfully")
#     else:
#         if not regphone:
#             messages.info(request,"Phone Invalid Plz Enter an Egyptian Phone Number ex:010..|011..|012..|015..")
#         elif not regpass:
#             messages.info(request,"Password Must be a letters or numbers and at least 6 characters")

#         return render(request,"regestrationforrestuarnt.html")
        


    
def Aboutus(request):
    return render (request,'aboutpage.html',{})     

# def login(request):
#     return render(request,'login.html')

def customer_reg (request):
    if request.method == "POST":
        cd2 = request.POST
        if get_user_model().objects.filter(email=cd2['email']) or get_user_model().objects.filter(username=cd2['full_name']):
            messages.warning(request, 'email or name used before')
            return redirect('customerreg')
        obj2 = Customer()
        obj2.user = get_user_model().objects.create_user(username=cd2['full_name'])
        obj2.user.email = cd2['email']
        obj2.user.set_password(cd2['password'])
        obj2.user.save()
        obj2.phone = cd2['phone']
        obj2.Area = cd2.get("area")
        obj2.City = cd2.get("city")
        obj2.save()
        messages.success(request, 'Registeration is successfully')
        return redirect('customerlogin')

    return render(request,'regcustomer.html',{})


def customer_login(request):
    cd = request.POST

    if request.method == "POST":
        user = authenticate(request, username=get_user_model().objects.filter(email=cd['email'])[0].username, password=cd['password'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid Email or Password')
            return redirect('customerlogin')

    return render(request, 'login.html', {})

# def User(request):
#          C_Fname=request.POST['fname']
#          C_Lname=request.POST['lname']
#          C_Email=request.POST['email']
#          C_Password =request.POST['password']
#          C_Password2=request.POST['Rpassword']
#          C_Phone=request.POST['phone']
#          C_City=request.POST['city']
#          C_Area =request.POST['area']
#          regphone=re.match(r"01(0|1|2|5)[0-9]{8}", C_Phone)
#         #  regname=re.match("^[a-zA-Z]*$",C_Fname)
#         #  if not regname:
#         #      messages.error(request,"name must be vaild")
#         #      return render (request,'registercustomer.html')
#          if C_Password == C_Password2 and regphone:
#             NewUser=models.Customer(C_Fname=C_Fname,C_Lname=C_Lname,C_Email=C_Email,
#               C_Password=C_Password,C_Password2=C_Password2,C_Phone=C_Phone,C_City=C_City,C_Area=C_Area)
#             NewUser.save()
#             messages.info(request,"Successfully Registered")
#             return render(request,'registercustomer.html')
#          else:
#             if C_Password != C_Password2:
#                 messages.error(request,"Password must be equal Retype Password")
#                 return render(request,'registercustomer.html')
#             elif not regphone:
#                 messages.error(request,"phone must be egypt")
#                 return render (request,'registercustomer.html')



#             #  messages.error(request,"passwod must be equal Retypepassword")
#             #  return render (request,'registercustomer.html')
#         #  elif not regphone:
#         #       messages.error(request,"phone must be egypt")
#         #       return render (request,'registercustomer.html')
        
         
            


#function for connect login page with database
# def curentuser(request):
#     if request.method=="POST":
#         try:
#             Userdetails=models.Customer.objects.get(C_Email=request.POST['email'],C_Password=request.POST['password'])
#             request.session['email']=Userdetails.C_Email
#             return render(request,'Mubarak html files/mainpage.html')
#         except models.Customer.DoesNotExist as e:
#             messages.success(request,'username/password invaild.........') 
#     return render(request,'login.html')

# def newUser(request):
#     if request.method=="POST":    
#         try:
#             userrest=models.Restaurant.objects.get(user.email=request.POST['email'],R_Password=request.POST['pass']) 
#             request.session['email']=userrest.user.email
#             return render(request,'Mubarak html files/mainpage.html',{'userrest':userrest})
#         except models.Restaurant.DoesNotExist as e:
#             messages.success(request,'Email or Password Invalid') 
#     return render(request,'loginForRestuarant.html')  

# def loginRestuarnt(request):
#     return render(request,'loginForRestuarant.html',{})

def loginType(request):
    return render(request,'loginType.html',{})


def logout_user(request):
    logout(request)
    return redirect('/')


#function for forget password page#
# def forgetpass(request):
#     return render(request,'forgetpassword.html') 

# # def changepass(request):
# #     if request.method=="POST":
# #         try:
# #             Userdetail=models.Customer.objects.get(C_Email=request.POST['email'])
# #             request.session['email']=Userdetail.C_Email
# #             return render(request,'Mubarak html files/mainpage.html')
# #         except models.Customer.DoesNotExist as e:
# #             messages.success(request,'username invaild.........') 
# #     return render(request,'forgetpassword.html')             
