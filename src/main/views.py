from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from main.models import Listing
from .forms import ListingForm
from users.forms import LocationForm
from .filters import ListingFilter

def main_view(request):
    return render(request, "views/main.html", {"name": "CarVibe"})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listing_filter': listing_filter
    }
    return render(request, "views/home.html", context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception('Form validation failed')
        except Exception as e:
            print(e)
            messages.error(request, 'An error occurred while posting the listing')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form})

@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        return render(request, 'views/listing.html', {'listing': listing})
    except Listing.DoesNotExist:
        messages.error(request, f'Invalid UID {id} was provided for listing')
        return redirect('home')

@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(request, f'Listing {id} updated successfully!')
                return redirect('home')
            else:
                messages.error(request, 'An error occurred trying to edit the listing!')
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)

        context = {
            'listing_form': listing_form,
            'location_form': location_form
        }
        return render(request, 'views/edit.html', context)
    except Listing.DoesNotExist:
        messages.error(request, f'Listing with id {id} does not exist!')
        return redirect('home')
