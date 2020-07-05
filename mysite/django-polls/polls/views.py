from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
def index(request):
    return render(request,'polls/index.html')