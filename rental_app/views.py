from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm,loginForm,owned_cars,search,bookings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import owned_cars as carModel,bookings as bookModel
from django.contrib.auth.models import User
import re
# Create your views here.
match=re.search
def home(request):
    form = UserRegistrationForm()
    Lform= loginForm()
    check='False' 
    errorMess=False
    SearchCar=search(request.GET)
    opt=None
    Display_cars=carModel.objects.all()
    checkM=Display_cars.values_list('make',flat=True)
    option=None
    name=None
    email=None
    bookObj=bookModel()
    book=bookings()
    obj2=bookModel.objects.all()
    checkPs=obj2.values_list('cars',flat=True)
    
    
    if request.method == 'POST' and 'SgU' in request.POST:
        form = UserRegistrationForm(request.POST)  
        Lform= loginForm()      
        if form.is_valid():
            form.save()
            user=authenticate(request,username=Lform.data.get('username'),password=Lform.data.get('password'))
            if user is not None:
                login(request,user) 
                return redirect('rental_app-rentals')
        else:
            check='True'
    elif request.method == 'POST' and 'SgI' in request.POST:
        form = UserRegistrationForm()
        Lform= loginForm(request.POST)
        user=authenticate(request,username=Lform.data.get('username'),password=Lform.data.get('password'))
        if user is not None:
            login(request,user)
            messages.success(request,'sent successfully')
            return redirect('rental_app-rentals')
        else:
            check='True2'
            errorMess='Enter correct Username or Password'
            messages.error(request,'could not log into account')
    elif request.method == 'GET' and 'DispBook'  in request.GET:
        check='True3'
        name=request.GET['DispBook'] 
        obj3=carModel.objects.filter(pk=name).first()
        temp=User.objects.filter(pk=obj3.user.id).first()
        bookObj=bookModel(user=temp,cars=obj3)
        book=bookings(instance=bookObj)   
        email=temp.email
    elif request.method == 'GET' and 'SRH'  in request.GET:
        opt=SearchCar.data.get('searchF')
        option=[i for i in checkM if match(opt.lower(),i.lower()) and i != ' ']
        if option:
            pass
        else:
            option=False
    elif request.method == 'POST' and 'BK' in request.POST:        
        book=bookings(request.POST,instance=bookObj)
        if book.is_valid():
            check='False'
            book.save()
            messages.success(request,'sent successfully')
        else:
            check='True3'
            messages.error(request,'could not send request')
    return render(request,'rental_app/home.html',
    {'Regform':form,'checkP':checkPs,'Logform':Lform,'check':check,'msg':errorMess,'DispCars':Display_cars,'sh':SearchCar,'opt':option,'Lender':email,'DateB':book})




def rentals(request):
    user_id=None
    delt=None
    delt2=None
    carsid=None
    reqc=bookModel.objects.filter(user=request.user)    
    if reqc:
        carsid=reqc.values_list('cars',flat=True) 
    cars=carModel.objects.filter(user=request.user)

    """ if request.user.is_authenticated:
        user_id=request.user.id """

    obj=carModel(user=request.user)
    Cform=owned_cars(instance=obj)
    DispCar=carModel.objects.filter(user=request.user)
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('rental_app-home')
    elif request.method == 'POST' and 'Det' in request.POST:        
        Cform=owned_cars(request.POST,request.FILES)
        if Cform.is_valid():
            Cform.save()
        else:
            messages.error(request,f'could not send for ')
    elif request.method == 'GET' and 'Delete' in request.GET:
        delt=request.GET['Delete']
        obj4=carModel.objects.filter(id=delt).first()
        obj4.delete()
    elif request.method == 'GET' and 'available' in request.GET:
        delt2=request.GET['available']
        obj5=bookModel.objects.filter(id=delt2).first()    
        obj5.delete()
        reqc=bookModel.objects.filter(user=request.user)  
    return render(request,'rental_app/rental_page.html',
    {'CarForm':Cform,'car_disp':DispCar,'reqc':reqc,'cars':cars,'Crid':carsid})    
