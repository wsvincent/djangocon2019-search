from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank
)
from django.views.generic import FormView, ListView
from .forms import SearchForm
from .models import City

class HomepageView(FormView):
    template_name = 'home.html'
    form_class = SearchForm

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    ## SearchRank ##
    def get_queryset(self):
        query = self.request.GET.get('q')
        vector = SearchVector('state')
        search_query = SearchQuery(query)
        object_list = City.objects.annotate(
            rank=SearchRank(vector, search_query)
        ).order_by('-rank')
        return object_list

    ## SearchQuery ##
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     object_list = City.objects.annotate(
    #         search=SearchVector('name', 'state'),
    #     ).filter(search=SearchQuery(query))
    #     return object_list

    ## SearchVector ##
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     object_list = City.objects.annotate(
    #         search=SearchVector('name', 'state'),
    #     ).filter(search=query)
    #     return object_list
