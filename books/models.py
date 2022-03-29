from pyexpat import model
from statistics import mode
import turtle
from unicodedata import category
from venv import create
from django.db import models

# Create your models here.
# Veritabanı ile ilişkiyi sağlar
# on_delete => bir yazar silindiğinde onunla ilişkili kitapları da veritabanından siliyor


class Author(models.Model):
    #Çıktı almak için fonksiyon yazıyoruz ve shelli sonra tekrar çalıştırıyoruz.
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,verbose_name="Yazar İsmi", null= False)
    created = models.DateTimeField('Oluşturulma Tarihi', null= False)
    about = models.CharField(max_length=1000,verbose_name="Yazar Hakkında",null=False)
    image = models.CharField(max_length=150,null=True,verbose_name="Yazar Fotoğrafı")


# İlişkisel model oluşturmak; 
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,verbose_name="Kategori İsmi", null= False)
    created = models.DateTimeField('Oluşturulma Tarihi', null= False)
    

class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,verbose_name="Kitap İsmi", null= False)
    created = models.DateTimeField('Oluşturulma Tarihi', null= False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name="Yazar İsmi", null= False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null= False,verbose_name="Kategori İsmi")
    image = models.CharField(max_length=150,null=True,verbose_name="Kitap Fotoğrafı")
    price = models.DecimalField(decimal_places=2,max_digits=4,null=False,verbose_name="Ürün Fiyatı")

class Setting(models.Model):
    def __str__(self):
            return self.title
    title = models.CharField(max_length=50,verbose_name="Website Title", null= False)
    description = models.CharField(max_length=160,verbose_name="Website Description", null= False)
    logo = models.CharField(max_length=150,verbose_name="Website Logo", null= False)
    favicon = models.CharField(max_length=150,verbose_name="Website Favicon", null= False)
    

# python manage.py runserver => projeyi başlatır
# django-admin startproject newproject => yeni proje oluşturur
# python manage.py migrate , python manage.py makemigrations books
# python manage.py sqlserver books 0002
# python manage.py shell
# from books.models import Book,Author
# from django.utils import timezone
# FİLTRELEME =>
# Author.objects.all() => Tüm verileri getirir array biçiminde
# Author.objects.filter(id=2) => id=2 olan veriyi getirir
# Author.objects.filter(name__startswith="D") => D ile başlayan verileri getirir
# endswith de belirtilen harf ile biten veriyi getirir
# created__year=2022 diye de filtreleme yaparız
# timezone.now().year => Bulunulan yılı gösterir
# author = Author.objects.get(id=1) => Tek bir veriyi döndürür
# author.book_set.all() ilişkisel biçimde o yazara ait kitapları listeliyoruz
# book.delete() => ilgili kitabı siler
# python manage.py createsuperuser => Admin kullanıcı oluşturma
# app oluşturma => python manage.py startapp books
# model => veritabanı ile entegrasyonu sağlar
# views => kullanıcıya göstereceğimiz görüntü
# settings.py sayfasındaki time_zone ve language güncellenmeli
# python manage.py migrate => veritabanı tablolarını oluşturuyor
# oluşturulan modelin apps içindeki config classı settings içinde tanımlanmalı
# python manage.py makemigrations books ile modellerimizi veritabanına tanımlıyoruz
# python manage.py sqlmigrate books 0001 => veritabanına göndeme işlemi

