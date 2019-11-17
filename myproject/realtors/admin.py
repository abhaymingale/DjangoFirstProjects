from django.contrib import admin

# Register your models here.
from .models import Realtors

# Register your models here.


class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_display_links = ('id', 'name')
    list_per_page = 10
    search_fields = ('phone', 'name')


admin.site.register(Realtors, RealtorsAdmin)
