from django.shortcuts import render, redirect, get_object_or_404
from .models import Donors
from .forms import DonorForm
from django.core.paginator import Paginator
from django.urls import reverse
from donations.models import DonationCollection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render())
    return render(request, "donors/index.html")


def donor_list(request):
    donor_queryset = Donors.objects.all().order_by('id')
    paginator = Paginator(donor_queryset, 10)
    page_number = request.GET.get('page', 1)
    donors_page = paginator.get_page(page_number)
    return render(request, "donor_list.html", {"donors": donors_page})

def create_donor(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("donor_list")
    else:
        form = DonorForm()
    return render(request, "create_donor.html", {"form": form})

def update_donor(request, pk):
    donor = get_object_or_404(Donors, pk=pk)
    if request.method == "POST":
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect("donor_list")
    else:
        form = DonorForm(instance=donor)
    return render(request, "update_donor.html", {"form": form})

def delete_donor(request, pk):
    donor = get_object_or_404(Donors, pk=pk)
    if request.method == "POST":
        donor.delete()
        return redirect("donor_list")
    return render(request, "delete_donor.html", {"donor": donor})

def donation_list(request):
    donation_url = reverse('donation_list') 
    donations = DonationCollection.objects.all()
    return render(request, 'donors/donation_list.html', {'donations': donations})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'donors/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         donor = Donors.objects.filter(username=username).first()
#         if donor and check_password(password, donor.password):
#             request.session['user_id'] = donor.id
#             if donor.role == 'organisation':
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('donor_dashboard')
#         else:
#             messages.error(request, "Invalid username or password.")
#     return render(request, 'donors/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('donor_dashboard')
    return render(request, 'donors/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def donor_dashboard(request):
    user = Donors.objects.get(id=request.session.get('user_id'))
    user_donations = DonationCollection.objects.filter(donor=request.user)
    return render(request, 'donors/donor_dashboard.html', {'donations': user_donations})

@login_required
def admin_dashboard(request):
    user = Donors.objects.get(id=request.session.get('user_id'))
    if request.user.role != 'organisation':
        return redirect('donor_dashboard')
    all_donations = DonationCollection.objects.all()
    return render(request, 'donors/admin_dashboard.html', {'donations': all_donations})
