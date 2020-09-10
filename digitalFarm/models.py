from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

#Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='SOME STRING')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.CharField(max_length=100, default='SOME STRING')

    category_choices = (
        ('fruits', 'Fruits'),
        ('nuts', 'Nuts'),
        ('tea', 'Tea'),
        ('oil', 'Oil'),
        ('flowers', 'Flowers'),
        ('veggies', 'Veggies'),
        ('honey', 'Honey'),
        ('legumes', 'Legumes'),
        ('wheat', 'Wheat'),
        ('mushroom', 'Mushroom'),
    )

    fruit_choices= (
        ('apple', 'apple'),
        ('orange', 'orange'),
        ('strawberry', 'strawberry'),
        ('coconut', 'coconut'),
        ('watermelon', 'watermelon'),
        ('banana', 'banana'),
        ('peach', 'peach'),
        ('kiwi', 'kiwi'),
        ('avocado', 'avocado'),
        ('cherry', 'cherry'),
    )
    veggie_choices= (
        (1, 'Avocado Bean'),
        (2, 'Broccoli'),
        (3, 'Carrot'),
        (4, 'Corn'),
        (5, 'Potatoe'),
        (6, 'Fresh Bean'),
        (7, 'cabbage'),
        (8, 'Cucumber'),
        (9, 'Eggplant'),
        (10, 'Tomatoes'),
    )
    city_choices= (
        ('Istanbul', 'Istanbul'),
        ('Denizli', 'Denizli'),
        ('Aydin', 'Aydin'),
        ('Izmir', 'Izmir'),
        ('Antalya', 'Antalya'),
        ('Rize', 'Rize'),
    )
    field_name = (
        ('GMO Free', 'Organic'),
        ('Fairtrade'),
    )
    #subcategory = models.ManyToManyField(Subcategory, blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, choices=Category.category_choices)  # parent
    #item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)  # productitem of category
    category = models.CharField(max_length=15, choices=category_choices, default=0) #onetomany? one category has multiple products
    city = models.CharField(max_length=15, choices=city_choices, default=0)
    product = models.CharField(max_length=15, choices=fruit_choices, default=0)
    product_type = models.CharField(max_length=15, blank=True, default='SOME STRING')
    amount = models.IntegerField(blank=True, default='SOME STRING')
    price = models.IntegerField(blank=True, default='SOME STRING')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('digitalFarm-detail', kwargs={'pk': self.pk})

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('digitalFarm-detail', kwargs={'pk': self.pk})

