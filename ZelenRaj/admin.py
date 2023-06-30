from django.contrib import admin
from .models import Plant, Order, PlantOrder


class PlantAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        # Checking if the user is a seller-superuser
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        # Checking if the user is a seller-superuser
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Checking if the user is a seller-superuser
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Plant, PlantAdmin)
admin.site.register(Order)
admin.site.register(PlantOrder)

