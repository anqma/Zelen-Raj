from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='plant_images/')
    price = models.IntegerField()
    care_info = models.TextField()
    stock = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    delivery_address = models.CharField(max_length=200)
    contact_information = models.CharField(max_length=100)
    payment_method = models.BooleanField(
        choices=[(True, 'Електронско плаќање'), (False, 'Плаќање во готово при достава')])
    note = models.TextField(max_length=200, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)


class PlantOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
