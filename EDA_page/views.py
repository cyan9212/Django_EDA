import django.http
from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    return render(request, 'index.html', {})

def data_page_view(request):
    return render(request, 'data_info_page.html', {})

def visualization_page_view(request):
    return render(request, 'visualization_page.html', {})