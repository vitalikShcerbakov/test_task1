from django.shortcuts import render

from .models import Contact

def index(request):
    contacts_list = Contact.objects.all()
    return render(request, 'contacts/index.html',
                  context={
                      'contacts_list': contacts_list
                      })


def contact_detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render(request, 'contacts/contact_detail.html',
                  context={
                      'contact': contact
                      })
