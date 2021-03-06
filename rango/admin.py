from csv import list_dialects
from pkgutil import extend_path
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.

class PageAdmin(admin.ModelAdmin):
   list_disxplay = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
