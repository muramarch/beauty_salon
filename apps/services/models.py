from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    # Другие поля для информации о категории

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(default=30, help_text="Duration of the service in minutes")
    # Другие поля для информации о услугах

    def __str__(self):
        return self.name

    def get_duration_minutes(self):
        return self.duration_minutes
