from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Legkovoe_Avto)
class Legkovoe_Avto_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(City)
class City_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Marka_Legkovoe_Avto)
admin.site.register(Model_Legkovoe_Avto)
admin.site.register(Transport)
admin.site.register(Image_Legkovoe_Avto)