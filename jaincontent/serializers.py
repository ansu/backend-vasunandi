from rest_framework import serializers
from .models import Category, Employee, SubCategory, Item

from django.contrib.auth.hashers import make_password




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = ['employee_id', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        emp = Employee.objects.create_user(**validated_data)
        return emp


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['emp_id', 'display_name', 'name', 'is_dashboard', 'is_side_menu','is_subcategory', 'type', 'logo','order_number']

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id', 'name', 'display_name', 'is_dashboard', 'is_side_menu','is_subcategory', 'type', 'logo','order_number']

    


class GetSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ['id', 'category_id', 'name', 'type', 'logo','order_number']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ['emp_id','category_id', 'name', 'type', 'logo','order_number']
 
    def create(self, validated_data):
        subcategory = SubCategory.objects.create(**validated_data)
        return subcategory


class GetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = ['id', 'title', 'subtitle', 'logo', 'link', 'description']



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = ['emp_id','category_id','sub_category_id', 'title', 'subtitle', 'logo','link','description']
 
    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        return item

