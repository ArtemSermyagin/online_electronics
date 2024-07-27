from django.contrib import admin
from .models import Network, Contact, Product, Country, City
from django.utils.html import format_html

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
        cities = City.objects.all()
        result = [(city.id, city.name) for city in cities]
        return result

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city_id=self.value())
        return queryset


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_network', 'liability', 'created_at')
    inlines = [ProductInline, ContactInline]
    list_filter = (NetworkCityFilter,)
    actions = ['clear_liability']

    def clear_liability(modeladmin, request, queryset):
        queryset.update(liability=0)

    clear_liability.short_description = "Очистить задолженность"

    def link_network(self, obj):
        return format_html(
            '<a href="{id}/change/">{name}</a>',
            id=obj.network.id if hasattr(obj.network, "id") else obj.id,
            name=obj.network
        )

    link_network.short_description = "Поставщик"

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    list_filter = ('country',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'city', 'street', 'house_number', 'network')
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'launch_date', 'network')
