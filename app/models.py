from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICES=(
  ('CR','Crud'),
  ('ML','Milk'),
  ('LS','Lassi'),
  ('MS','MilkShake'),
  ('PN','Panner'),
  ('GH','Ghee'),
  ('CZ','cheese'),
  ('IC','Ice Cream'),
  
)
STATE_CHOICES=(
  ('Alabama','Alaska'),
  ('Arizona','Arkansas'),
  ('California','Colorado'),
  ('Connecticut','Delaware')
)
class product(models.Model):
  title=models.CharField(max_length=100)
  selling_price=models.FloatField()
  descounted_price=models.FloatField()
  description= models.CharField(max_length=100)
  prodapp=models.TextField(default='')
  category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
  product_image=models.ImageField(upload_to='product/')
  def __str__(self):
    return self.title

class Customer(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  locality=models.CharField(max_length=200)
  city=models.CharField(max_length=50)
  mobile=models.IntegerField(default=0)
  zipcode=models.IntegerField()
  state=models.CharField(choices=STATE_CHOICES,max_length=100)
  def __str__(self):
      return self.name
  
  
  
