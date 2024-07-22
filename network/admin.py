from django.contrib import admin
from .models import Network, Contacts, Products

class ContactsInline(admin.TabularInline):
    model = Contacts

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'liability', 'time_creation')
    list_filter = ('city',)
    inlines = [ContactsInline]

    def clear_liability(modeladmin, request, queryset):
        queryset.update(liability=0)
    clear_liability.short_description = "Очистить задолженность"

admin.site.register(Network, NetworkAdmin)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('network', 'country', 'email')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'model')