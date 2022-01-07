import django.http
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
# Create your views here.
def main_page_view(request):
    return render(request, 'index.html', {})

def graph_view(request):
    fig, ax = plt.figure(figsize=(10, 10))
    canvas = FigureCanvas(fig)
    label = [1,2,3]
    value = [10,20,30]
    sns.barplot(x=label, y=value)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return render(request, 'graph_page.html', {'image':response})