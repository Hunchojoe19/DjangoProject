from django.contrib import admin
from .models import Book, Publisher


# Register your models here.
class MyAppAdminSite(admin.ModelAdmin):
    site_header = "My App",
    site_title = "My Book App"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    list_filter = ['publisher', 'date_published']
    search_fields = ['title', 'isbn_exact', 'publisher__name__startswith']
    list_per_page = 10  # for pagination

    # fields = ['title', 'isbn']

    # admin.site.register(Book, BookAdmin)
    admin.site.register(Publisher)
