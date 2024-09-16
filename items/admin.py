from django.contrib import admin
from .models import Legkovoe_Avto, Marka_Legkovoe_Avto, Model_Legkovoe_Avto, Transport
# Register your models here.



@admin.register(Legkovoe_Avto)
class Legkovoe_Avto_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Marka_Legkovoe_Avto)
admin.site.register(Model_Legkovoe_Avto)
admin.site.register(Transport)