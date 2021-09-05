from django.contrib import admin
from jwt_token_task.models import Category, Product


@admin.register(Category, Product)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
