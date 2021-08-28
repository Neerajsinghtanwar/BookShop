from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from .middlewares import underconstructionmiddleware
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'app/index.html')


@underconstructionmiddleware
def about(request):
    pass


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        email = request.POST.get("email_id")
        phone = request.POST.get("phone_no.")
        desc = request.POST.get("desc")
        if fname != '' and lname != '' and email != '' and phone != '':
            details = Contact(fname=fname, lname=lname, email=email, phone=phone, desc=desc )
            details.save()
            messages.success(request, "We will contact you soon!!")
        else:
            messages.error(request, "Field are empty!!")
    return render(request, 'app/contact.html')


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your account is created")
    else:
        fm = SignUpForm()
    return render(request , 'app/signup.html', {'form':fm})


def user_login(request):
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        fm = LoginForm()
    return render(request, 'app/login.html', {'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def addbook(request):
    if request.user.is_staff==True:
        form = BookForm()
        if request.method=='POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Book added successfully")
        return render(request, 'app/add_book.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


@login_required
def update_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "*Book updated successfuly!!")
    else:
        book = Book.objects.get(pk=id)
        form = BookForm(instance=book)
    return render(request, 'app/update_book.html', {'form':form})


@login_required
def view_books(request):
        book = Book.objects.all().order_by('price')
        paginator = Paginator(book, 6)
        page_num = request.GET.get('page')
        books = paginator.get_page(page_num)
        return render(request, 'app/view_book.html', {'books':books})


def delete_book(request, id):
    if request.method == 'POST':
        pi = Book.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/viewbooks/')


@login_required
def purchase_book(request, id):
    if request.method=='POST':
        book = Book.objects.get(pk=id)
        form = PurchaseBookForm(request.POST, instance=book)
        if form.is_valid():
            obj = PurchaseBook(customername=form.cleaned_data['customername'], bookname=form.cleaned_data['bookname'], address=form.cleaned_data['address'], price=form.cleaned_data['price'])
            obj.save()
            messages.success(request, "Book purchased successfully")
    else:
        book = Book.objects.get(pk=id)
        form = PurchaseBookForm(instance=book)
    return render(request, 'app/purchase_book.html', {'form': form})

@login_required
def view_purchased_books(request):
        books = PurchaseBook.objects.filter(customername=request.user).order_by('date')
        paginator = Paginator(books, 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        return render(request, 'app/purchased_books.html', {'books':page_obj})


def userprofile(request):
    fm = UserDetailForm(instance=request.user)
    return render(request, 'app/userprofile.html', {'form':fm})


def edituserprofile(request):
    if request.method == 'POST':
        fm = UserDetailForm(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Profile edit successfully!!")
    else:
        fm = UserDetailForm(instance=request.user)
    return render(request, 'app/edituserprofile.html', {'form':fm})
