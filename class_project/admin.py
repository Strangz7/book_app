from django.contrib import admin

from .models import Book, Publisher


class MyAppAdminSite(admin.AdminSite):
    site_title = "My Book App"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']
    # fieldsets = ({'date': ('date_published',)}, {'name': ('title', 'isbn')})


# admin.site.register(Book)
admin.site.register(Publisher)
