from django.contrib import admin
from testapp.models import Author, Info_author, Book
# Register your models here.

admin.site.register(Author)
admin.site.register(Info_author)
admin.site.register(Book)
