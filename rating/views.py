from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SimpleForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Rating

class RatingsListView(ListView):
    # model = Rating
    queryset = Rating.objects.all()
    context_object_name = 'rating_objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_context'] = 'Foo'
        return context
    
class RatingEntryListView(ListView):
    template_name = 'rating/rating_by_name.html'
    context_object_name = 'rating_name_objects'

    def get_queryset(self):
        return Rating.objects.filter(name=self.kwargs['name'])

@method_decorator(login_required, name = 'dispatch')
class SimpleView(View):
    name = 'Anonymous'

    def get(self, request):
        return HttpResponse(f'Hello, {self.name}')

class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'initial value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')

        return render(request, self.template_name, {'form':form})
    
class RatingDetailView(DetailView):
    model = Rating
