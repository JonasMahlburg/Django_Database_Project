from django.contrib import admin
from .models import Customer, Product, Producttype, Order, Bill

class CustomerAdmin(admin.ModelAdmin):
    list_filter=["first_name", "last_name"]
    list_display=["first_name", "last_name"]
    readonly_fields=["account"]
    prepopulated_fields={"slug":["first_name", "last_name"]}
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo", "slug"],
            },
        ),
    ]


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Order)
admin.site.register(Bill)