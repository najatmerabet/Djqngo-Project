from django.contrib import admin
from .models import Customer, product
# Register your models here.
@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
  list_display=['id','title','descounted_price','category','product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
  list_display=['id','user','locality','city','state','zipcode']