"""
URL configuration for searchpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from searchapp.views import search_books, update_book, delete_book
from django.contrib import admin 

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', search_books, name='search_books'),
    path('book/update/<int:book_id>/', update_book, name='update_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
    # Other URL patterns...
]
