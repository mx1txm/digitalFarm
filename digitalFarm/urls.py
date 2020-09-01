from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, FilterView
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='digitalFarm-home'),
    path('', PostListView.as_view(), name='digitalFarm-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='digitalFarm-detail'),
    path('post/new/', PostCreateView.as_view(), name='digitalFarm-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='digitalFarm-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='digitalFarm-delete'),
    path('about/', views.about, name='digitalFarm-about'),
    path('filter/', FilterView.as_view(), name='digitalFarm-filter'),
    path('users/', views.list_all, name='digitalFarm-list_all'),
    path('categories/', views.categories, name='digitalFarm-categories'),
    path('vegetable/', views.vegetable, name='digitalFarm-vegetable'),
    path('fruits/', views.fruits, name='digitalFarm-fruits'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)