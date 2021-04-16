from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    id = models.AutoField(primary_key=True)

    display_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.display_name} ({self.user})"
       

