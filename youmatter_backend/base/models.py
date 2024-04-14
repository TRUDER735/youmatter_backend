import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_surnme = models.CharField(max_length=100)
    admin_email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    # admin_emailpassword = models.CharField(max_length=100)
    admin_code = models.CharField(max_length=10)


    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    agent_name = models.CharField(max_length=100)
    agent_surnme = models.CharField(max_length=100)
    agent_email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    # agent_emailpassword = models.CharField(max_length=100)
    agent_code = models.CharField(max_length=10)
    agent_location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    client_name = models.CharField(max_length=100)
    client_surnme = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)
    client_phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

