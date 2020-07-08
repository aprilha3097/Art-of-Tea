from django.contrib import admin
from .models import Order, OrderItemDetails


class OrderItemDetailsAdminInline(admin.TabularInline):
    # allows to add/edit order items in the admin panel inside the OrderModel
    model = OrderItemDetails
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemDetailsAdminInline,)

    readonly_fields = ('order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'grand_total',)
    # fields allows to specify the order of the fields in the admin interface
    fields = ('order_number', 'full_name',
              'email', 'phone_number', 'address_line1', 'address_line2',
              'town_or_city', 'county', 'country',
              'postcode', 'purchase_date', 'delivery_cost',
              'order_total', 'grand_total',)
    # restrict the columns that show up in the order list to only few key items
    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # displays most recent orders on the top
    ordering = ('-purchase_date',)


admin.site.register(Order, OrderAdmin)