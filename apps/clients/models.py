from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    # Другие поля для информации о клиенте

    def __str__(self):
        return self.name
