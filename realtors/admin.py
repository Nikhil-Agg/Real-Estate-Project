from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = ('email', 'phone', 'is_mvp',)
    list_filter = ('name',)
    list_per_page = 25
    search_fields = ('name', 'email', 'phone')

admin.site.register(Realtor, RealtorAdmin)
