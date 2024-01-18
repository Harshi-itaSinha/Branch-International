from django.db import models

# Create your models here.

class Complaint(models.Model):
    name = models.TextField()
    phone_number = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField()
    order_date = models.DateField()
    product_category = models.TextField()
    product_name = models.TextField()
    question = models.TextField()
    feedback = models.TextField(null=True, blank=True)
    complain_date = models.DateTimeField(auto_now_add=True)