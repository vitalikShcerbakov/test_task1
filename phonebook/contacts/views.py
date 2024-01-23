import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, SearchForm, SubdivisionForm
from .models import Contact


def index(request):
    search_form = SearchForm()

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        contacts_list = Contact.objects.filter(full_name__icontains=search_query)
    else:
        contacts_list = Contact.objects.all()

    context = {
        'search_form': search_form,
        'contacts_list': contacts_list,
    }
    return render(request, 'contacts/index.html', context)


def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/contact_detail.html',
                  context={
                      'contact': contact})


def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contacts:index')
    return render(request, 'contacts/create_or_update_contact.html',
                  {'form': form, 'contact': contact, 'is_edit': True})


def contact_creat(request):
    form = ContactForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('contacts:index')
    return render(request,
                  'contacts/create_or_update_contact.html',
                  {'form': form})


def contact_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:index')
    return render(request,
                  'contacts/contact_delete.html',
                  {'contact': contact})


def subdivision_creat(request):
    form = SubdivisionForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('contacts:index')
    return render(request, 'contacts/add_subdivision.html', {'form': form})


def export_data(request):
    queryset = Contact.objects.all()
    serialized_data = serialize('json', queryset)
    json_data = json.loads(serialized_data)

    filename = 'exported_data.json'
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

    with open(filename, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
