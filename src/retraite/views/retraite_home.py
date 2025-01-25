from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'retraite/index.html')

@login_required
def retraite(request):
    return render(request, 'retraite/retraite_home.html')


