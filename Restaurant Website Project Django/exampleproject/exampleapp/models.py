# Inside models.py of your app

# Inside models.py of your app

from django.db import models

class MenuItem(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    @staticmethod
    def get_all_products():
        return MenuItem.objects.all()
    
    @staticmethod
    def get_products_by_id(ids):
        return MenuItem.objects.filter(id__in =ids)
