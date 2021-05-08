from django.shortcuts import render,HttpResponse,redirect
from . import models
import re
from django.contrib import messages
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant,FoodItem,Customer,Order
# from .models import vindour,food





# Create your views here.



        #       Mubarak Functions workplace        #

    # Main page functions
def mainpage(request):
    Restobject = Restaurant.objects.all()
    Foods = FoodItem.objects.all()
    
    return render(request,'Mubarak html files/mainPage.html',{
        'Restobject': Restobject[0:3],
         'Foods': Foods[0:3],
         }
         )

    # Restaurant page functions 

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
        print('customer orders variable -----')
        print(customers_orders)
        if customers_orders:
            recive_orders = customers_orders
            print('recive orders variabel ----')
            print(recive_orders)
        else:
            recive_orders = 'thers is no orders for today'
            # print(recive_orders)

    else:
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
            print('food item variable')
            print(food_item)
            
        #     return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {})
        # else:
        #     return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {})
    return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {
        #  to show current Restaurant data
        'R_id'      : Restaurant_id.id,
        'R_Image'   : Restaurant_id.R_Image,
        'R_Name'    : Restaurant_id.R_Name,
        'R_Type'    : Restaurant_id.R_Type,
        'R_Email'   : Restaurant_id.R_Email,
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
        


    return render(request, 'Mubarak html files/ManyToMany/restaurant.html', {
        #  to show current Restaurant data
        'R_id'      : Restaurant_id.id,
        'R_Image'   : Restaurant_id.R_Image,
        'R_Name'    : Restaurant_id.R_Name,
        'R_Type'    : Restaurant_id.R_Type,
        'R_Email'   : Restaurant_id.R_Email,
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
def history_of_orders(request, id):
        #  global variables for if condations 
    customerinfo = None
    history  = None
    message  = None

        #  get and check the user 
    checkuesr = Customer.objects.get(id=id)
    if checkuesr:
        customerinfo = Customer.objects.get(id=id)
        # print((customerinfo.C_Fname))
        history= Order.objects.all().filter(customers__id=id)
        message = 'ther is no orders'
        if history:
            print(history)
        
        else:
            pass

        if customerinfo:
            pass
    

    return render(request, 'Mubarak html files/ManyToMany/customersOrders.html', {
        'customerinfo': customerinfo,
        'history' : history,
        'message' : message
    })





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


@csrf_exempt
def Outer_SearchBox(request):
    if request.method == "POST":
        outer_search = request.POST.get('searched')

        Rlist = Restaurant.objects.all().filter(R_Name__iexact=outer_search)
        Rlist_two = Restaurant.objects.all().filter(R_Name__istartswith=outer_search[0])

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
    order = FoodItem.objects.get(id=id)
    if request.method == "POST":
        # print(order)
        orders = Order(
            D_Name = order.It_Name,
            D_totalCost = order.It_Prise,
        )
        orders.save()
        # print(orders)
        A = Customer.objects.all()
        # print(A[0].id)
        orders.customers.add(A[0].id)

        return render(request, 'Mubarak html files/OrdersPage.html', {
            'order': order,
            'orderName': order.It_Name,
            'orderKink': order.It_Kind,
            'orderSize': order.It_Prise,
            'orderDescription': order.It_Descrip,
            'orderImages': order.F_Images,
            'orderRate': order.F_Rate
        })
    else:
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
    return render(request,'regestrationforrestuarnt.html',{})

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


def delete(request,id):
    obj = FoodItem.objects.get(id=id)
    obj.delete()
    return redirect('/restaurant')


def afterReg(request):
    res_name=request.POST['restname']
    res_type=request.POST['restype']
    res_email=request.POST['email']
    res_password=request.POST['pass']
    res_phone=request.POST['phone']
    res_city=request.POST['city']
    res_area=request.POST['area']
       # error_message=None
    # if not res_name:
    #     error_message="Restuarant Name Is Required"
    # elif len(res_name)<2:
    #         error_message="Restuarant Name must be 2 char or more "

    # elif res_type:
    #     error_message="Restuarant Type Is Required"
    # elif not res_email:
    #     error_message=" Email Is Required"
    # elif not res_password:
    #     error_message="Password Is Required"
    # elif not res_phone:
    #     error_message="Phone Is Required"
    # elif not res_city:
    #     error_message="City Is Required"
    # elif not res_area:
    #     error_message="Area Is Required"
    regphone=re.match(r"01(0|1|2|5)[0-9]{8}",res_phone)
    regpass=re.match(r"^[a-z0-9]{6,20}$",res_password)
    if regphone and regpass:
        reg=models.Restaurant(R_Name=res_name,R_Type=res_type,R_Email=res_email,R_Password=res_password,
                R_Phone=res_phone,R_City=res_city,R_Area=res_area)
        reg.save()
        messages.info(request,"Successfully Registered")
        return render(request,"regestrationforrestuarnt.html")
        # return HttpResponse("Successfully")
    else:
        if not regphone:
            messages.info(request,"Phone Invalid Plz Enter an Egyptian Phone Number ex:010..|011..|012..|015..")
        elif not regpass:
            messages.info(request,"Password Must be a letters or numbers and at least 6 characters")

        return render(request,"regestrationforrestuarnt.html")
        


    
def Aboutus(request):
    return render (request,'aboutpage.html',{})     

def login(request):
    return render(request,'login.html')

def customer_reg (request):
    return render(request,'registercustomer.html')


def User(request):
         C_Fname=request.POST['fname']
         C_Lname=request.POST['lname']
         C_Email=request.POST['email']
         C_Password =request.POST['password']
         C_Password2=request.POST['Rpassword']
         C_Phone=request.POST['phone']
         C_City=request.POST['city']
         C_Area =request.POST['area']
         regphone=re.match(r"01(0|1|2|5)[0-9]{8}", C_Phone)
        #  regname=re.match("^[a-zA-Z]*$",C_Fname)
        #  if not regname:
        #      messages.error(request,"name must be vaild")
        #      return render (request,'registercustomer.html')
         if C_Password == C_Password2 and regphone:
            NewUser=models.Customer(C_Fname=C_Fname,C_Lname=C_Lname,C_Email=C_Email,
              C_Password=C_Password,C_Password2=C_Password2,C_Phone=C_Phone,C_City=C_City,C_Area=C_Area)
            NewUser.save()
            messages.info(request,"Successfully Registered")
            return render(request,'registercustomer.html')
         else:
            if C_Password != C_Password2:
                messages.error(request,"Password must be equal Retype Password")
                return render(request,'registercustomer.html')
            elif not regphone:
                messages.error(request,"phone must be egypt")
                return render (request,'registercustomer.html')



            #  messages.error(request,"passwod must be equal Retypepassword")
            #  return render (request,'registercustomer.html')
        #  elif not regphone:
        #       messages.error(request,"phone must be egypt")
        #       return render (request,'registercustomer.html')
        
         
            


#function for connect login page with database
def curentuser(request):
    if request.method=="POST":
        try:
            Userdetails=models.Customer.objects.get(C_Email=request.POST['email'],C_Password=request.POST['password'])
            request.session['email']=Userdetails.C_Email
            return render(request,'Mubarak html files/mainpage.html')
        except models.Customer.DoesNotExist as e:
            messages.success(request,'username/password invaild.........') 
    return render(request,'login.html')

def newUser(request):
    if request.method=="POST":    
        try:
            userrest=models.Restaurant.objects.get(R_Email=request.POST['email'],R_Password=request.POST['pass']) 
            request.session['email']=userrest.R_Email
            return render(request,'Mubarak html files/mainpage.html',{'userrest':userrest})
        except models.Restaurant.DoesNotExist as e:
            messages.success(request,'Email or Password Invalid') 
    return render(request,'loginForRestuarant.html')  

def loginRestuarnt(request):
    return render(request,'loginForRestuarant.html',{})

def loginType(request):
    return render(request,'loginType.html',{})


#function for forget password page#
def forgetpass(request):
    return render(request,'forgetpassword.html') 

def changepass(request):
    if request.method=="POST":
        try:
            Userdetail=models.Customer.objects.get(C_Email=request.POST['email'])
            request.session['email']=Userdetail.C_Email
            return render(request,'Mubarak html files/mainpage.html')
        except models.Customer.DoesNotExist as e:
            messages.success(request,'username invaild.........') 
    return render(request,'forgetpassword.html')             
