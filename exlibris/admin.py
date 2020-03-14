from django.contrib import admin
from .models import Author, Biography, Book, Reader, Lend

# Register your models here.

admin.site.register(Author)
admin.site.register(Biography)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Lend)