from django.conf.urls import url
from .views import  RegisterView, CategoryView,SubCategoryView, ItemView

urlpatterns = [

   url(r'^get_categories/', CategoryView.as_view(), name='get_categories'),
   url(r'^get_subcategories/$', SubCategoryView.as_view(), name='get_sub_categories'),
   url(r'^get_items/$', ItemView.as_view(), name='get_items'),


   url(r'^register_item/', ItemView.as_view(), name='register_item'),
   url(r'^register_subcategory/', SubCategoryView.as_view(), name='register_subcategory'),
   url(r'^category/', CategoryView.as_view(), name='category'),
   url(r'^register/', RegisterView.as_view(), name='register'),
]
