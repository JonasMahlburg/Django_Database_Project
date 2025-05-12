from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Customer
from django.utils import timezone
# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    paginate_by = 3

class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name__icontains=name)

class CustomerDetailView(DetailView):
     model = Customer
     template_name = "sales/detail.html"

     def get_object(self):
         obj = super().get_object()
         obj.last_accessed = timezone.now()
         return obj