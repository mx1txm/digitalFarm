from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='SOME STRING')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.CharField(max_length=100, default='SOME STRING')

    category_choices= (
        ('Fruits', 'Veggies'),
        ('Nuts', 'Honey'),
        ('Tea', 'Legumes'),
        ('Oil', 'Wheat'),
        ('Flowers', 'Mushroom'),
    )
    fruit_choices= (
        ('apple', 'banana'),
        ('orange', 'peach'),
        ('strawberry', 'kiwi'),
        ('coconut', 'avocado'),
        ('watermelon', 'cherry'),
    )
    city_choices= (
        ('Istanbul', 'Izmir'),
        ('Denizli', 'Antalya'),
        ('Aydin', 'Rize'),
    )
    field_name = (
        ('GMO Free', 'Organic'),
        ('Fairtrade'),
    )

    category = models.CharField(max_length=15, choices=category_choices, default=category_choices[0][0])
    city = models.CharField(max_length=15, choices=city_choices, default=city_choices[0][0])
    product = models.CharField(max_length=15, choices=fruit_choices, default=fruit_choices[0][0])
    product_type = models.CharField(max_length=10, blank=True, default='SOME STRING')
    amount_av_min = models.CharField(max_length=10, blank=True, default='SOME STRING')
    amount_av_max = models.CharField(max_length=10, blank=True, default='SOME STRING')
    price_min = models.CharField(max_length=10, blank=True, default='SOME STRING')
    price_max = models.CharField(max_length=10, blank=True, default='SOME STRING')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('digitalFarm-detail', kwargs={'pk': self.pk})