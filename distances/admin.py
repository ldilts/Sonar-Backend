from django.contrib import admin

# Register your models here.
from .models import Distance

class DistanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['dist_id', 'dist_distance']}),
        ('Date information', {'fields': ['dist_date']}),
    ]

    list_display = ('dist_id', 'dist_distance', 'dist_date', 'was_published_recently')
    list_filter = ['dist_date']
    # search_fields = ['log_open']

admin.site.register(Distance, DistanceAdmin)