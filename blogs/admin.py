from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title', 'category')
    list_filter = ('category', 'created_at')

