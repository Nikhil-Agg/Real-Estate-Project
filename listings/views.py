from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
from .choices import state_choices, bedroom_choices, price_choices

# Create your views here.
def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_listing = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listing = queryset_listing.filter(description__icontains=keywords)
    
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_listing = queryset_listing.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_listing = queryset_listing.filter(state__iexact=state)
    
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_listing = queryset_listing.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_listing = queryset_listing.filter(price__lte=price)
 
    context = {
        'listings': queryset_listing,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)