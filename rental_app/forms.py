from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import owned_cars,bookings
import datetime

dateT=datetime.date.today()
class UserRegistrationForm(UserCreationForm):
    """ password1=forms.PasswordInput()
    password2=forms.PasswordInput() """ 
    def __init__(self,*args, **kwargs):
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput,forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder':field.label})
                elif type(field.widget) is forms.PasswordInput:
                    field.widget = forms.PasswordInput(attrs={'placeholder':field.label})
                elif type(field.widget) is forms.EmailInput:
                    field.widget = forms.EmailInput(attrs={'placeholder':field.label})

    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class loginForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','id':'userlogin'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model=User
        fields=('username','password')
class owned_cars(forms.ModelForm):
    #user=forms.CharField(widget=forms.TextInput())    
    class Meta:
        model = owned_cars  
        fields = ("car_image","make","price_per_day","location","user")
class search(forms.Form):
    searchF=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Car name','id':'my_search','name':'searching'}),required=False)
class bookings(forms.ModelForm):
   Pick_up_date=forms.DateTimeField(input_formats=[r'%Y-%m-%d'],
       widget=forms.DateTimeInput(attrs={'placeholder':'dd/mm/yyyy','type':'date','min':dateT}),required=True)
   Return_date=forms.DateTimeField(input_formats=[r'%Y-%m-%d'],widget=forms.DateTimeInput(attrs={'placeholder':'dd/mm/yyyy','type':'date','min':dateT}),required=True)
   class Meta:
       model=bookings
       fields='__all__'