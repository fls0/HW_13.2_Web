from django.urls import path, include

from . import views
from .views import quotes, author_info

app_name = "quotesapp"

urlpatterns = [
    path('', quotes, name='quotes'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>/', views.author_info, name='author_info'),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name='tag_quotes')

]