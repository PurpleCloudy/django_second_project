from django.shortcuts import render
from rating.models import Rating

# Create your views here.
def pagination_view(request, *args, **kwargs):
    qs = Rating.objects.all()
    page = int(request.GET.get('page', 1))
    paginate_by = 5
    start_index = (page*paginate_by) - paginate_by
    end_index = page*paginate_by
    return render(request, 'pagination_example/pagination_example.html', {'data_list':qs[start_index:end_index], 'previous_page':page-1 or 1, 'next_page':page+1, 'page':page})

