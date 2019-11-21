from django.shortcuts import render

from django.http import HttpResponse

from listings.models import Listing

from realtors.models import Realtors

# Create your views here.


def index(request):
    listing = Listing.objects.order_by('-List_date').filter()[:3]
    context = {
        'listing': listing
    }
    print(context)
    return render(request, 'pages/index.html', context)


def about(request):
    single_realtor = Realtors.objects.filter(is_mvp=True)
    all_realtor = Realtors.objects.all()
    context = {
        'singlerealtor': single_realtor[0],
        'all_realtor': all_realtor
    }
    print(context)
    return render(request, 'pages/about.html', context)
