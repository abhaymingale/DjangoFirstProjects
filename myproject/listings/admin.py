from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'Is_publish', 'price',  'realtors')
    list_display_links = ('id', 'title')
    list_filter = ('realtors',)
    list_editable = ('Is_publish',)
    list_per_page = 10
    search_fields = ('title', 'price')


admin.site.register(Listing, ListingAdmin)
