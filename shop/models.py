from django.db import models

# Create your models here.
class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    productCategory = models.CharField(max_length=50,default="")
    productDescription = models.CharField(max_length=400)
    productPrice = models.FloatField()
    publishDate = models.DateField()

    def __str__(self) :
        return self.productName

