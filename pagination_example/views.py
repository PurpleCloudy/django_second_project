from django.shortcuts import render
from rating.models import Rating

# Create your views here.
def pagination_view(request, *args, **kwargs):
    qs = Rating.objects.all()
    return render(request, 'pagination_example/pagination_example.html', {'data_list':qs})