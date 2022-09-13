from django.shortcuts import render
from django.views.generic import View
from django.db.models.query import QuerySet
from django.core.exceptions import ImproperlyConfigured
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

class BasicListView(View):
    model = None
    queryset = None
    template_name = None

    def get(self, request, *args, **kwargs):
        if self.model:
            objects = self.queryset.all()
            context = {"object_list": objects}
        else:
            context = {"object_list": None}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        if self.model:
            objects = self.queryset.all()
            context = {"object_list": objects}
        else:
            context = {"object_list": None}
        return render(request, self.template_name, context)
    
    def delete(self, request, *args, **kwargs):
        if self.model:
            objects = self.queryset.all()
            context = {"object_list": objects}
        else:
            context = {"object_list": None}
        return render(request, self.template_name, context)
    
    def put(self, request, *args, **kwargs):
        if self.model:
            objects = self.queryset.all()
            context = {"object_list": objects}
        else:
            context = {"object_list": None}
        return render(request, self.template_name, context)

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
        queryset = queryset.order_by(*ordering)
        return queryset

    def get_ordering(self):
        pass

    def paginate_queryset(serializer, request, queryset, page, limit=20):
        """Build a paginated response for a given queryset."""
        paginator = Paginator(queryset, 20)
        try:
            tracks = paginator.page(page)
        except PageNotAnInteger:
            tracks = paginator.page(1)
        except EmptyPage:
            tracks = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer_obj = serializer(
            tracks, context=serializer_context
        )

        return serializer_obj.data