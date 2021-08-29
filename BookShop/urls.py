"""BookShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addbook/', views.addbook, name='addbook'),
    path('viewbooks/', views.view_books, name='viewbooks'),
    path('search/', views.search_books, name='search'),
    path('deletebook/<int:id>', views.delete_book, name='deletebook'),
    path('updatebook/<int:id>', views.update_book, name='updatebook'),
    path('purchasebook/<int:id>', views.purchase_book, name='purchasebook'),
    path('viewpurchasedbooks/', views.view_purchased_books, name= 'viewpurchasedbooks'),
    path('profile', views.userprofile, name='userprofile'),
    path('editprofile', views.edituserprofile, name='edituserprofile'),
]