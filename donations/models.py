from django.db import models
# from donors.models import Donors
# from django.contrib.auth.models import User

class DonationCollection(models.Model):
    donor = models.ForeignKey('donors.Donors', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField()
    donation_method = models.CharField(max_length=100) 
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.donor.username} - {self.amount} on {self.donation_date}"
