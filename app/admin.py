from django.contrib import admin

# Register your models here.
from .models import CustomUser, Code

admin.site.register(Code)
@admin.register(CustomUser)
class Custom(admin.ModelAdmin):
    list_display = ['id', 'username', 'region', 'is_active']
    list_filter = ['first_name', 'region', 'is_active']
    search_fields = ['username', 'region']

    def save_model(self, request, obj, form, change):
        if len(str(obj.password)) < 20:
            obj.set_password(obj.password)
        super(Custom, self).save_model(request, obj, form, change)