from django.contrib import admin
from .models import customUser
# Register your models here.

class customUser_Display(admin.ModelAdmin):
    list_display=["username","city"]
    search_fields=["city"]
    
    
