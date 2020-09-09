import django_filters

from digitalFarm.models import Post
from django_filters import DateFilter
from .models import *

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    date_posted = django_filters.DateFilter(input_formats=['%Y-%m-%d','%d-%m-%Y'],lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='iexact')
    city_choices = django_filters.ChoiceFilter(field_name='city', lookup_expr='iexact')
    category = django_filters.ChoiceFilter(field_name='category', lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['title', 'author']#, 'category', 'city'

from .models import Snippet

class SnippetFilter(django_filters.FilterSet):

    class Meta:
        model = Snippet
        fields = ('title', 'body','created')