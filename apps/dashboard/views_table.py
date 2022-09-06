# Create your views here.
from dashboard.base.basiclistview import BasicListView


class TableView(BasicListView):
    model = None
    template_name = 'dashboard/tables.html'