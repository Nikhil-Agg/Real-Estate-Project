from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_editable = ('is_published',)
    list_display_links = ('id', 'title',)
    list_filter = ('realtor', 'city',)
    list_per_page = 25
    search_fields = ('title', 'price', 'city', 'state', 'zipcode')


admin.site.register(Listing, ListingAdmin)
