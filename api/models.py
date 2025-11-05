from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"