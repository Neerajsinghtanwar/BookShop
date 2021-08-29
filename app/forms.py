from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import *
from rest_framework.authtoken.models import Token


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User     
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email','user_type':'You are'}
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'user_type':forms.Select(attrs={'class':'form-control'}),
        }

    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
        'bookname':forms.TextInput(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control'}),
        'quantity':forms.TextInput(attrs={'class':'form-control'}),
        'price':forms.TextInput(attrs={'class':'form-control'}),
        }

class PurchaseBookForm(forms.ModelForm):
    class Meta:
        model = PurchaseBook
        fields = "__all__"
        labels = {'customername':'Name'}
        widgets = {
        'customername':forms.TextInput(attrs={'class':'form-control'}),
        'bookname':forms.TextInput(attrs={'class':'form-control'}),
        'price':forms.TextInput(attrs={'class':'form-control'}),
        'date':forms.DateInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        }



class UserDetailForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
        labels = {'email':'Email'}
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'date_joined':forms.DateInput(attrs={'class':'form-control'}),
        }