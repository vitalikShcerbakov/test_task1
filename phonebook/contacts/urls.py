from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/<int:contact_id>/',
         views.contact_detail, name='contact_detail'),
    path('subdivision_creat/',
         views.subdivision_creat, name='subdivision_creat'),
    path('add_contact/',
         views.contact_creat, name='add_contact'),
    path('contact_edit/<int:contact_id>/',
         views.contact_edit, name='contact_edit'),
    path('contact_delete/<int:contact_id>/',
         views.contact_delete, name='contact_delete'),
    path('export_data/', views.export_data, name='export_data'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
