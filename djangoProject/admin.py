from django.contrib import admin


class DjangoProjectAdminSite(admin.AdminSite):
    site_title = "BookBout Admin Site"
    site_header = "Welcome to the BookBout Admin Interface"
    index_title = "BookBout Index"