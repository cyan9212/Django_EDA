import django.http
from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    return render(request, 'index.html', {})

def data_info_view(request):
    return render(request, 'data_info_page.html', {})
