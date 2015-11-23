from django.contrib import admin

# Register your models here.
from .models import Log

class LogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['log_id', 'log_open']}),
        ('Date information', {'fields': ['log_date']}),
    ]

    list_display = ('log_id', 'log_open', 'log_date', 'was_published_recently')
    list_filter = ['log_date']
    # search_fields = ['log_open']

admin.site.register(Log, LogAdmin)