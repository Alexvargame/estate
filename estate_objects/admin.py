from django.contrib import admin

from .models import City, Street, District, Flat,House,Smartflat

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=('city', 'region', 'country')

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display=('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display=('city', 'street', 'district')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=('city', 'street', 'district')

@admin.register(Smartflat)
class SmartflatAdmin(admin.ModelAdmin):
    list_display=('city', 'street', 'district')




