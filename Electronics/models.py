from django.db import models

# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length = 10 , primary_key=True)
    email = models.EmailField()
    MobileNo = models.PositiveIntegerField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Vendor(models.Model):
    username = models.CharField(max_length = 10 , primary_key=True)
    email = models.EmailField()
    MobileNo = models.PositiveIntegerField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Mobiles(models.Model):
    catagory = models.CharField(default = 'Mobile',max_length=11)
    brand_name = models.CharField(max_length=10)
    name = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    Specifications = models.TextField()
    img=models.ImageField(upload_to='pro/mobiles')
    review=models.TextField()

    def __str__(self):
        return self.name

class Accessories(models.Model):
    catagory = models.CharField(default = 'Laptop',max_length=11)
    brand_name = models.CharField(max_length=10)
    name = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    Specifications = models.TextField()
    img=models.ImageField(upload_to='pro/accessories')
    review=models.TextField()

    def __str__(self):
        return self.name

class Laptops(models.Model):
    catagory = models.CharField(default = 'Accessories' , max_length=11)
    brand_name = models.CharField(max_length=10)
    name = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    Specifications = models.TextField()
    img=models.ImageField(upload_to='pro/laptops')
    review=models.TextField()

    def __str__(self):
        return self.name


    
