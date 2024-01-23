from django.db import models


class Subdivision(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'Подр: {self.name} ({self.description})'


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(
        'фото',
        upload_to='photo/',
        blank=True
    )
    phone = models.CharField(max_length=10)
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='contacts'
    )

    def __str__(self):
        return self.full_name
