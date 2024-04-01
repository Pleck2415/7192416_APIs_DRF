from django.contrib import admin
from shop.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('userName', 'active')


# class ProductAdmin(admin.ModelAdmin):

#     list_display = ('name', 'category', 'active')


# class ArticleAdmin(admin.ModelAdmin):

#     list_display = ('name', 'product', 'category', 'active')

#     @admin.display(description='Category')
#     def category(self, obj):
#         return obj.product.category


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
