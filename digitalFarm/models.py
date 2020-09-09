from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

#Category
#from django.utils.text import slugify


#class Category(models.Model):
    #name= models.CharField(max_length=20)
    #category = models.Choices(category_choices)
    #slug = models.SlugField(verbose_name='Slug')
    #category = models.ForeignKey( #parent
        #"self",
        #on_delete=models.CASCADE,
        #null=True,
        #blank=True,
        #related_name="Item",
    #)
    #class Meta:
    #    ordering = ('name',)
    #    verbose_name = 'category'
     #   verbose_name_plural = 'categories'

    #def __str__(self):
     #   return self.name

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
    #    super(Category, self).save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('shop:product_list_by_category',
    #                   args=[self.slug])

#DEFAULT_CAT_ID = 1
#Subcategory
#class Item(models.Model):
    #name = models.CharField(max_length=20)
    #category = models.ForeignKey(Category, related_name='item', on_delete=models.CASCADE, blank=True,
                             #null=True, verbose_name='Select category', default=None)
    #slug = models.SlugField(unique=True, null=True)

    #class Meta:
        #verbose_name_plural = 'subcategory'

    #def __str__(self):
        #return self.name
#Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='SOME STRING')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.CharField(max_length=100, default='SOME STRING')

    category_choices = (
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
    #MEDIA_CHOICES = (
    #    ('Fruits', (
    #        ('apple', 'Apple'),
    #        ('banana', 'Banana'),
    #    )
     #    ),
    #    ('Veggies', (
    #        ('cucumber', 'Cucumber'),
    #        ('eggplant', 'Eggplant'),
    #    )
    #     ),
    #)
    field_name = (
        ('GMO Free', 'Organic'),
        ('Fairtrade'),
    )

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, choices=Category.category_choices)  # parent
    #item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)  # productitem of category
    category = models.CharField(max_length=15, choices=category_choices, default=0) #onetomany? one category has multiple products
    #subcategory = models.ManyToManyField(Subcategory, blank=True)

    city = models.CharField(max_length=15, choices=city_choices, default=0)
    product = models.CharField(max_length=15, choices=fruit_choices, default=0)
    product_type = models.CharField(max_length=15, blank=True, default='SOME STRING')
    amount = models.CharField(max_length=15, blank=True, default='SOME STRING')
    price = models.CharField(max_length=15, blank=True, default='SOME STRING')

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

