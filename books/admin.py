from django.contrib import admin

admin.site.site_header="Yönetim Paneli"
admin.site.site_title="Yönetim Paneli"
admin.site.index_title="D&R Book Store"

# Register your models here.
# Admin Paneline modellerimizin yönetimini ekliyoruz
from .models import Author
from .models import Book
from .models import Category
from .models import Setting


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Setting)


