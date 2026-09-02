from django.db import models
from datetime import date
# Create your models here.

class Category(models.Model):
    category = models.CharField("カテゴリー",max_length=20)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    image = models.ImageField("商品画像",)
    Date  = models.DateField("登録日",)
    categorys = models.ForeignKey(Category,verbose_name = "カテゴリー",on_delete = models.PROTECT)
    limit  =  models.DateField ("期限",)
    product_name = models.CharField("商品名",max_length=100)
    maker =  models.CharField("メーカー",max_length=100)
    num  =  models.IntegerField("個数",)
    price  = models.IntegerField("値段",)
    memo   = models.TextField("メモ",)
    recommend  = models.BooleanField("マイ防災グッズリスト",)
    link  = models.URLField("URL",)
    
    
    
    def __str__(self):
        return self.title