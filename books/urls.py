from importlib.resources import path


from django.urls import path
from. import views

urlpatterns = [
    path('',views.index, name='index'),
    path('authors',views.authors, name='authors'),
    path('books',views.books, name='books'),
    path('authordetails/<int:authorId>',views.authorDetails, name='authorDetails'),
    path('bookdetails/<int:bookId>',views.bookDetails, name='bookDetails'),
    path('categorydetails/<int:categoryId>',views.categoryDetails, name='categoryDetails')
    
    
]
