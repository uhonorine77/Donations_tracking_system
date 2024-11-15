from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser

class Donors(models.Model):
    ROLES = (
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('organisation', 'Organisation'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_donation_date = models.DateTimeField(null=True, blank=True)
    preferred_donation_method = models.CharField(max_length=50, choices=[('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer')], default='Credit Card')
    role = models.CharField(max_length=15, choices=ROLES, default='individual')
    password = models.CharField(max_length=120)
    
    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username