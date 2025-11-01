from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'department', 'location',
        'work_mode', 'job_type', 'posted_on'
    )
    list_filter = (
        'department', 'location', 'work_mode',
        'job_type', 'posted_on'
    )
    search_fields = (
        'title', 'department', 'location', 'tags', 'description'
    )
    readonly_fields = ('posted_on',)
    ordering = ('-posted_on',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'department', 'location', 'work_mode', 'job_type')
        }),
        ('Content', {
            'fields': ('description', 'details', 'tags')
        }),
        ('Metadata', {
            'fields': ('posted_on',)
        }),
    )
