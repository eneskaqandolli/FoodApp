from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=250)
    item_price = models.IntegerField()
    image = models.ImageField(upload_to="images", null=True)
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    
