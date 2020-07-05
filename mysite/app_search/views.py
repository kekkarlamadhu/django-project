from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import AppInfo,KeyWordData
from django.db.models import Q
#from .forms import *
from django.http import *
# Create your views here.
# cities/views.py
from django.views.generic import TemplateView, ListView

def Home(request):
    obj = AppInfo.objects
    return render(request,'app_search/home.html', {'obj': obj})

def App_details(request,id):
    app_detail = get_object_or_404(AppInfo, pk=id)
    return render(request, 'app_search/App_details.html', {'app': app_detail})

class SearchResultsView(ListView):
    model = AppInfo
    template_name = 'app_search/search_keyword.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = AppInfo.objects.filter(
            Q(app_name__icontains=query) | Q(app_type__icontains=query)
        )
        return object_list
def Google(request):
    obj1 = AppInfo.objects
    return render(request,'app_search/googleplay_store.html', {'obj': obj1})