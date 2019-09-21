from django.db.models import Q # new
from django.views.generic import TemplateView, ListView, FormView
from .models import City
from .forms import SearchForm

class HomepageView(FormView): # new
    template_name = 'home.html'
    form_class = SearchForm # new

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    # def get_queryset(self): # new
    #     query = self.request.GET.get('q')
    #     object_list = City.objects.filter(
	# 	      Q(name__icontains=query) | Q(state__icontains=query)
	#     )
    #     return object_list
    def get_queryset(self): # new
        return City.objects.filter(
            Q(name__icontains='Boston') | Q(state__icontains='NY')
        )
