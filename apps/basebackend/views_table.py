# Create your views here.
from django.views.generic import ListView

class TableView(ListView):
    model = None
    template_name = 'basebackend/tables.html'

    def get_queryset(self):
        if self.model:       
            return self.model.objects.order_by('-population')[0:self.kwargs['num_of_countries']]
        return