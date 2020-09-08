from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, FilterView, SnippedListView
from . import views
from users.views import deleteuser

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('search/', views.filter_list, name='search'),
    path('filter/', views.filter_list, name='digitalFarm-filter'),
    #path('filter/', FilterView.as_view(), name='digitalFarm-filter'),
    path('snippet/', SnippedListView.as_view(), name='snippet'),
    path('', views.home, name='digitalFarm-home'),
    path('', PostListView.as_view(), name='digitalFarm-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='digitalFarm-detail'),
    path('post/new/', PostCreateView.as_view(), name='digitalFarm-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='digitalFarm-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='digitalFarm-delete'),
    path('about/', views.about, name='digitalFarm-about'),
    path('users/', views.list_all, name='digitalFarm-list_all'),
    path('categories/', views.categories, name='digitalFarm-categories'),
    path('fruits/', views.fruits, name='digitalFarm-fruits'),
    path('vegetable/', views.vegetable, name='digitalFarm-vegetable'),
    path('allium/', views.allium, name='digitalFarm-allium'),
    path('berries/', views.berries, name='digitalFarm-berries'),
    path('grains/', views.grains, name='digitalFarm-grains'),
    path('greens/', views.greens, name='digitalFarm-greens'),
    path('honey/', views.honey, name='digitalFarm-honey'),
    path('legumes/', views.legumes, name='digitalFarm-legumes'),
    path('nuts/', views.nuts, name='digitalFarm-nuts'),
    path('oil/', views.oil, name='digitalFarm-oil'),
    path('spices/', views.spices, name='digitalFarm-spices'),
    path('tea/', views.tea, name='digitalFarm-tea'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)