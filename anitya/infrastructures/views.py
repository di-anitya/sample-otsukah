from django.views import generic
from django.urls import reverse_lazy
from .models import Driver, Physical, Virtual
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DriverForm
from bootstrap_modal_forms.generic import BSModalCreateView

class DriverListView(LoginRequiredMixin, generic.ListView):
    template_name = 'infrastructures/driver/index.html'
    context_object_name = 'latest_driver_list'
    paginate_by = 10

    def get_queryset(self):
        return Driver.objects.all()


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    template_name = 'infrastructures/driver/detail.html'


class DriverRegisterView(BSModalCreateView):
    template_name = 'infrastructures/driver/edit.html'
    form_class = DriverForm
    success_message = 'Success: Driver was created.'
    success_url = reverse_lazy('infrastructures:driver_list')



class PhysicalListView(LoginRequiredMixin, generic.ListView):
    template_name = 'infrastructures/physical/index.html'
    context_object_name = 'latest_physical_list'
    paginate_by = 10

    def get_queryset(self):
        return Physical.objects.all()


class PhysicalDetailView(LoginRequiredMixin, generic.DetailView):
    model = Physical
    template_name = 'infrastructures/physical/detail.html'


class VirtualListView(LoginRequiredMixin, generic.ListView):
    template_name = 'infrastructures/virtual/index.html'
    context_object_name = 'latest_virtual_list'
    paginate_by = 10

    def get_queryset(self):
        return Virtual.objects.all()


class VirtualDetailView(LoginRequiredMixin, generic.DetailView):
    model = Virtual
    template_name = 'infrastructures/virtual/detail.html'
