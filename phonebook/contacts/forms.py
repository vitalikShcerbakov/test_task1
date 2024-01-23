from django.forms import ModelForm

from .models import Contact, Subdivision


class SubdivisionForm(ModelForm):
    """
    Класс формы нового подразделения.
    """
    class Meta:
        model = Subdivision
        labels = {
            'name': 'Номер Подразделения',
            'description': 'Описание'
        }

        fields = ('name', 'description',)


class ContactForm(ModelForm):
    """
    Класс формы Контакта.
    """

    class Meta:
        model = Contact
        labels = {
            'full_name': 'Полное имя',
            'phone': 'Телефон',
            'subdivision': 'Подразделение',
            'photo': 'Фотография'
        }

        fields = ('full_name', 'phone', 'subdivision', 'photo')
