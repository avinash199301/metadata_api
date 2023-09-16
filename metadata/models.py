from django.db import models

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
class SKU(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
