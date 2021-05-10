from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView

from .models import Company, Employee
from .forms import EmployeeForm
# Create your views here.

def index(request):
    return HttpResponse('Yay I made a request return http response')


def app_home(request):
    return render(request, 'demoapp/base_demoapp.html')


#company list function view
def company_list(request):
    companies = Company.objects.all()
    context = {'object_list': companies}
    return render(request, 'demoapp/company_list.html', context=context)


#company list class based view
class CompanyView(View):

    def get(self, request):
        companies = Company.objects.all()
        context = {'object_list': companies}
        return render(request, 'demoapp/company_list.html', context=context)


#company list generic class based view
class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #so we can use the same form as create, but change create button text to update
        context['is_update'] = True
        return context


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('demoapp:company_list')


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name_suffix = '_update_form'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('demoapp:company_list')