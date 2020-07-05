from django.contrib import admin
from .models import AppInfo,KeyWordData
# Register your models here.
class Search_Admin(admin.ModelAdmin):
    list_display = ("app_name", "app_type",)
admin.site.register(AppInfo,Search_Admin)