from django.shortcuts import render, redirect
from .models import DonationCollection
from .forms import DonationCollectionForm

def donation_list(request):
    if request.user.is_authenticated and request.user.role == 'admin':
        donations = DonationCollection.objects.all()
    else:
        donations = DonationCollection.objects.filter(donor=request.user)
    return render(request, 'donations/donation_list.html', {'donations': donations})

def create_donations(request):
    if request.method == 'POST':
        form = DonationCollectionForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.save()
            return redirect('donation_list')
    else:
        form = DonationCollectionForm()
    return render(request, 'donations/create_donations.html', {'form': form})
