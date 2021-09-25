from django.contrib import admin

from .models import *

from django.forms.models import BaseInlineFormSet

# class CategoryTemplateAdmin(admin.ModelAdmin):
#     fields = ['category', 'field_name']
class ProductCharacteristicInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        instance = kwargs['instance']
        field_names = instance.productcharacteristic_set.all().values_list('field_name', flat=True)
        initial = []
        for c in CategoryTemplate.objects.all().values('field_name'):
            if c['field_name'] not in field_names:
                initial.append(c)

        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    formset = ProductCharacteristicInlineFormSet
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductCharacteristicInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Feedback)
admin.site.register(Category)
admin.site.register(CategoryTemplate)
admin.site.register(CategoryFilterValue)
admin.site.register(ProductCharacteristic)
