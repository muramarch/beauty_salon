from django.contrib.auth.models import User
from django.db import models


class Master(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='master_photos')

    def __str__(self):
        return self.user.username
    



