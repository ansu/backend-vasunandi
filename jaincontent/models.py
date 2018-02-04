from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
# Create your models here.

from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    ''' Manager to handle creation queries of the BaseUser Model '''
    def create(self, employee_id, password, is_admin, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not employee_id:
            raise ValueError('The given email must be set')
        user = self.model(
            employee_id=employee_id,
            is_active=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, employee_id, password=None, **extra_fields):
        return self.create(employee_id, password, False, False, **extra_fields)

    def create_superuser(self, employee_id, password,  **extra_fields):
        return self.create(employee_id, password, True, True, **extra_fields)


class Employee(AbstractBaseUser, PermissionsMixin):
    employee_id = models.PositiveIntegerField(unique=True, primary_key=True )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = "employee_id"

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return unicode(self.employee_id)




class Category(models.Model):

	CATEGORY_TYPES = (
	    ('list', 'list'),
	    ('News', 'News'),
	    ('content_list', 'content_list'),
	    ('gallery', 'gallery'),
	    ('video', 'video'),
	    ('pdf', 'pdf')
	)
	emp_id = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
	created_time = models.DateField(auto_now_add=True)
	name  = models.CharField(max_length=100)
	display_name  = models.CharField(max_length=100, default = "")
	is_dashboard = models.BooleanField(default=False)
	is_side_menu = models.BooleanField(default=False)
	is_subcategory =  models.BooleanField(default=False)
	type = models.CharField(max_length=20, choices=CATEGORY_TYPES, blank=True, null=True)
	logo = models.CharField(max_length=254, default="")
	is_deleted =  models.BooleanField(default=False)
	order_number = models.IntegerField(default = 100)


	def __unicode__(self):
		return unicode(self.name)


class SubCategory(models.Model):

	CATEGORY_TYPES = (
	    ('list', 'list'),
	    ('News', 'News'),
	    ('content_list', 'content_list'),
	    ('gallery', 'gallery'),
	    ('video', 'video'),
	    ('pdf', 'pdf')
	)
	emp_id = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
	category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	created_time = models.DateField(auto_now_add=True)
	name  = models.CharField(max_length=100)
	type = models.CharField(max_length=20, choices=CATEGORY_TYPES, blank=True, null=True)
	logo = models.CharField(max_length=254, default="")
	is_deleted =  models.BooleanField(default=False)
	order_number = models.IntegerField(default = 100)
	def __unicode__(self):
		return unicode(self.name)




class Item(models.Model):

	emp_id = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
	category_id = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	sub_category_id = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
	created_time = models.DateField(auto_now_add=True)
	title  = models.CharField(max_length=250)
	subtitle  = models.CharField(max_length=250)
	logo = models.CharField(max_length=254, default="")
	link = models.CharField(max_length=254, default="")
	description =  models.TextField(null=True, blank=True)
	is_deleted =  models.BooleanField(default=False)


	def __unicode__(self):
		return unicode(self.title)
