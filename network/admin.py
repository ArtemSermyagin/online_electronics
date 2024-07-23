from django.contrib import admin
from .models import Network, Contact, Product


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'network', 'liability', 'created_at')
    inlines = [ProductInline, ContactInline]

    # def clear_liability(modeladmin, request, queryset):
    #     queryset.update(liability=0)
    #
    # clear_liability.short_description = "Очистить задолженность"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number', 'network')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'launch_date', 'network')
