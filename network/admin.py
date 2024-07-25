from django.contrib import admin
from .models import Network, Contact, Product


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class NetworkCityFilter(admin.SimpleListFilter):
    title = 'Город'
    parameter_name = 'city_filter'

    def lookups(self, request, model_admin):
        return (
            ('value1', 'Тверь'),
            ('ммм', 'Сочи'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset
        return queryset


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'network', 'liability', 'created_at')
    inlines = [ProductInline, ContactInline]
    list_filter = (NetworkCityFilter,)
    # def clear_liability(modeladmin, request, queryset):
    #     queryset.update(liability=0)
    #
    # clear_liability.short_description = "Очистить задолженность"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number', 'network')
    list_filter = ('city',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'launch_date', 'network')
