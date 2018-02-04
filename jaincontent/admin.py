from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Category, SubCategory, Item


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('employee_id', 'first_name', 'last_name', 'password', 'is_admin')
admin.site.register(Employee, EmployeeAdmin)



class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'emp_id', 'name', 'display_name','is_dashboard', 'is_side_menu', 'is_subcategory', 'type', 'logo', 'is_deleted','order_number')
admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = ('id', 'emp_id', 'category_id', 'name', 'type', 'logo', 'is_deleted','order_number')

admin.site.register(SubCategory, SubCategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('id', 'category_id', 'sub_category_id', 'title', 'subtitle', 'description', 'logo', 'link', 'created_time', 'emp_id')


admin.site.register(Item, ItemAdmin)
