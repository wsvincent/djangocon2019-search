from django.urls import path
from .views import SearchResultsView, HomepageView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomepageView.as_view(), name='home'),
]
