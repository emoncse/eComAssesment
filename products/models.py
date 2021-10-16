from django.db import models


# Create your models here.
class Products(models.Model):
    product_id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=60, blank=False, null=False)
    price = models.FloatField()
    details = models.CharField(max_length=1000)
    viewCount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/', default='default.jpg')
