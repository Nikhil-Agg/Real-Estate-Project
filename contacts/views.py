from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # check if user has made same enquiry 
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'You have already enquired about the same property')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, 
        phone=phone, message=message, user_id=user_id)
        contact.save()

        messages.success(request, 'Your enquiry has been sent succesfully')

        return redirect('/listings/'+listing_id)