from django.contrib import admin
from .models import OrderForm, Items


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'id', 'position', 'quantity', 'state',)


# Register your models here.
admin.site.register(OrderForm)
admin.site.register(Items, ItemsAdmin)
# admin.site.register(OrderFormItems)
