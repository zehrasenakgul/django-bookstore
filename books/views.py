
from django.shortcuts import render
#Proje yollarını belirlemek için ihtiyacımız olan kütüphane:
from django.http import HttpResponse
from django.template import loader #html dosyalarını göstermek için
from .models import Author,Book,Setting,Category
from django.http import Http404
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'authors_list' : Author.objects.all(),
        'categories_list' : Category.objects.all(),
        'books_list' : Book.objects.all(),
        'setting' : Setting.objects.get(id=1)
    }
    return HttpResponse(template.render(context,request));

def authors(request):
    template = loader.get_template('authors.html')
    context = {
        'authors_list' : Author.objects.all(),
        'categories_list' : Category.objects.all(),
        'setting' : Setting.objects.get(id=1)

    }
    # direkt render fonksiyonu ile de çalışabiliriz
    # render(request,"authors.html",context) şeklinde
    return HttpResponse(template.render(context,request));

def books(request):
    return HttpResponse("Kitaplar");

def authorDetails(request,authorId):
    try:
        context = {
            'author_detail' : Author.objects.get(pk=authorId),
            'setting' : Setting.objects.get(id=1),
            'categories_list' : Category.objects.all(),
        }
    except Author.DoesNotExist:
        raise Http404("Yazar Bulunamadı")
    return render(request,"authorDetail.html",context)

def categoryDetails(request,categoryId):
    template = loader.get_template('categoryDetail.html')
    try:
        context = {
            'category_detail' : Category.objects.get(pk=categoryId),
            'setting' : Setting.objects.get(id=1),
            'categories_list' : Category.objects.all(),
            'books_list': Book.objects.filter(category=categoryId)

        }
    except Category.DoesNotExist:
        raise Http404("Kategori Bulunamadı")
    return HttpResponse(template.render(context,request));
   
def bookDetails(request,bookId):
    template = loader.get_template('bookDetails.html')
    try:
        context = {
            'book_detail' : Book.objects.get(pk=bookId),
            'setting' : Setting.objects.get(id=1),
            'categories_list' : Category.objects.all(),

        }
    except Book.DoesNotExist:
        raise Http404("Kitap Bulunamadı")
    return HttpResponse(template.render(context,request));
   
