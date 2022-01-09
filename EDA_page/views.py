from django.shortcuts import render, HttpResponse
from .utils import get_graph, get_plot, get_hist, get_plot_hue, get_hist_hue, get_empty_plot
from .models import Features
from .form import FeatureForm

# Create your views here.
def main_page_view(request):
    return render(request, 'index.html', {})

def data_page_view(request):
    return render(request, 'data_info_page.html', {})

def visualization_page_view(request):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if 'feature1' in form.data and 'feature2' in form.data:
            if 'hue' in form.data:
                chart = get_plot_hue(form.data['feature1'], form.data['feature2'], form.data['hue'])
            else:
                chart = get_plot(form.data['feature1'], form.data['feature2'])

        elif 'feature1' in form.data and 'feature2' not in form.data:
            if 'hue' in form.data:
                chart = get_hist_hue(form.data['feature1'], form.data['hue'])
            else:
                chart = get_hist(form.data['feature1'])

        elif 'feature1' not in form.data and 'feature2' in form.data:
            if 'hue' in form.data:
                chart = get_hist_hue(form.data['feature2'], form.data['hue'])
            else:
                chart = get_hist(form.data['feature2'])

        else:
            chart = get_empty_plot()
        return render(request, 'visualization_page.html', {'chart': chart})


    x = 'HeartDisease'
    chart = get_hist(x)
    return render(request, 'visualization_page.html', {'chart': chart})