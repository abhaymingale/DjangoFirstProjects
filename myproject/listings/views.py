from django.shortcuts import render
from django.http import HttpResponse

from .models import Listing
# Create your views here.


def index(request):
    listing = Listing.objects.all()
    context = {
        'listing': listing
    }
    print(context)
    return render(request, 'listings/listings.html', context)


def listing(request, myid):
    print(myid)
    singlelisting = Listing.objects.filter(id=myid)
    print(singlelisting)
    singlelistingcontext = {
        'singlelisting': singlelisting[0]
    }
    print(singlelistingcontext)
    return render(request, 'listings/listing.html', singlelistingcontext)


def search(request):
    return render(request, 'listings/search.html')
