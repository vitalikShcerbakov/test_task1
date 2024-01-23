from django.contrib import admin

from .models import Contact, Subdivision


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone',)
    search_fields = ('full_name',)
    list_filter = ('phone',)
    empty_value_display = '-пусто-'

@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    pass
