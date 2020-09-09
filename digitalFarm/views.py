from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from .models import Post#, #Category,Item
from .forms import FilterForm
from .filters import ProductFilter


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all
    }
    print(context)
    return render(request, 'digitalFarm/home.html', context)

def list_all(request):
    context = {
        'users': User.objects.all
    }
    return render(request, 'users/list_all.html', context)

class ArticleListView(ListView):
    model = Post
    print("inside ArticleListView")
    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = ProductFilter(self.request.GET, queryset=qs)
        print(product_filtered_list)
        return product_filtered_list.qs

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter_list(request):#BootstrapFilterView(request)
    qs = Post.objects.all()
    categories = Post.category

    #fruits = Post.objects.filter(categories='Fruits')
    #veggies = Post.objects.filter(categories='Veggies')

    #subcategories = Category.objects.filter
    products = Post.product#.fruit_choices #Post.products
    city = Post.city_choices
    price = Post.price

    #subcategories = Category.objects.filter(parent_category__id=target_category.id)
    #print(Post.category)
    #filter = ProductFilter(request.GET, queryset= products)
    title_contains_query = request.GET.get('title_contains')
    categories_query = request.GET.get('category')
    #subcategories_query = request.GET.get('subcategory')
    product_query = request.GET.get('product')
    city_query = request.GET.get('city')
    price_query = request.GET.get('product')
    amount_query = request.GET.get('amount')
    #cat = Category.objects.all()
    #for sub_cat in cat.sub_categories.all():

    #parents = Category.objects.filter(parent=None)
    #parent = parents[0]  # create some categories before using it
    #childs = parent.childs.all()

    #date_min_query = request.GET.get('date_min')
    #date_max_query = request.GET.get('date_max')

    #Title
    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)
    #category
    if is_valid_queryparam(categories_query) and categories_query != 'Choose...':
        qs = qs.filter(category__iexact=categories_query)
    # subcategory
    #if is_valid_queryparam(subcategories_query) and subcategories_query != 'Choose...':
        #qs = qs.filter(subcategory__iexact=subcategories_query) #parent_category__id=target_category.id
    #product
    if is_valid_queryparam(product_query) and product_query != 'Choose...':
        qs = qs.filter(product__iexact=product_query)
    #city
    if is_valid_queryparam(city_query):
        qs = qs.filter(city__iexact=city_query)
    #price
    if is_valid_queryparam(price_query) and price_query != 'Price':
        qs = qs.filter(price__iexact=price_query)
    #Menge
    if is_valid_queryparam(amount_query) and amount_query != 'Menge':
        qs = qs.filter(amount__iexact=amount_query)

    #date_min
    #if is_valid_queryparam(date_min_query):
        #qs = qs.filter(date_posted__gte=date_min_query) #date_posted
    #date_max
    #if is_valid_queryparam(date_max_query):
        #qs = qs.filter(date_posted__lte=date_min_query)

    context = {
        'queryset': qs,
        'category' : categories,
        'product' : products,
        'city' : city,
        'price' : price,
    }

    #return render(request, 'digitalFarm/filter_list.html', {'filter': filter})
    return render(request, 'digitalFarm/filter_list.html', context)

#def category_list(request, slug):
#    category = Category.objects.get(slug=slug)
 #   products = ProductFilter(request.GET, queryset=Products.objects.filter(category=category)

   # return render(request, 'products/category_list.html', {"products":products, 'category': category})


def about(request):
    return render(request, 'digitalFarm/about.html', {'title': 'About'})

def categories(request):
    return render(request, 'digitalFarm/categories.html')

def fruits(request):
    return render(request, 'digitalFarm/category/fruits.html')

def vegetable(request):
    return render(request, 'digitalFarm/category/vegetable.html')

def allium(request):
    return render(request, 'digitalFarm/category/wurzelgemuese.html')

def berries(request):
    return render(request, 'digitalFarm/category/berries.html')

def grains(request):
    return render(request, 'digitalFarm/category/grains.html')

def greens(request):
    return render(request, 'digitalFarm/category/greens.html')

def honey(request):
    return render(request, 'digitalFarm/category/honey.html')

def legumes(request):
    return render(request, 'digitalFarm/category/legumes.html')

def nuts(request):
    return render(request, 'digitalFarm/category/nuts.html')

def oil(request):
    return render(request, 'digitalFarm/category/oil.html')

def spices(request):
    return render(request, 'digitalFarm/category/spices.html')

def tea(request):
    return render(request, 'digitalFarm/category/tea.html')

#all products- compares the value of the choosen category with the value/name of the post.category
def items(request):
    items = Post.objects.get(pk=request.GET.get('value'))#oder .filter()? #get(category.value or inputState.value=pk
    return render(request, 'filter_list.html', {'item': items})

class PostListView(ListView):
    model = Post
    template_name = 'digitalFarm/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordering posts from latest to oldest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'city', 'category', 'product', 'product_type', 'amount', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'city', 'category','product', 'product_type', 'amount', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #prevent that a user can update other users posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class FilterView(TemplateView):
    template_name = 'digitalFarm/filter.html'

    def filter(self, request): #get request
        form = FilterForm(request.GET)
        #form = FilterForm() #war vorher hashtag
        form.save()
        posts = Post.objects.all()
        title_contains = request.GET.get('title_contains')


        myFilter = ProductFilter(request.GET, queryset=posts)
        posts = myFilter.qs
        #return render(request, "digitalFarm/filter.html", posts)
        #return render(request, filter_list(), {'myFilter': myFilter})
            #return render(request, 'myfarm/filter.html')
        #return render(request, self.template_name, {'form': myFilter})
        return render(request, self.template_name, posts)
            #return render(request, self.template_name, )

    def post(self, request):
        form = FilterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            post = form.save()
            post.save()
            form = FilterForm()
            post = form.save()
            return redirect('filter:filter')

        args = {'form': form}
        return render(request, self.template_name, args)

from .models import Snippet
from .filters import SnippetFilter

class SnippedListView(ListView):
    model = Snippet
    template_name = 'snippet/snipped_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        print(context['filter'])

        return context

class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippet/snipped_detail.html'