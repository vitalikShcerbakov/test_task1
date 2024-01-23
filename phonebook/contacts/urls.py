from django.urls import path

from contacts import views


app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/<int:contact_id>/', views.contact_detail, name='contact_detail'),
]
