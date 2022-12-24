from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Work, Appliances
from .forms import WorkOrderForm, WorkOrderFormUpdate, WorkOrderPartUpdate
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

#def home(request):
#   return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})

class WorkOrders(ListView):
    model = Work
    template_name = 'work_orders.html'

class WorkOrderDetails(DetailView):
    model = Work
    template_name = 'work_order_details.html'

class CreateWorkOrder(SuccessMessageMixin, CreateView):
    model = Work
    form_class = WorkOrderForm
    template_name = 'create_work_order.html'
    
    def get_success_message(self, cleaned_data):
        return 'Work Order Created!'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdateWorkOrder(UpdateView):
    model = Work
    template_name = 'update_work_order.html'
    form_class = WorkOrderFormUpdate
    success_url = reverse_lazy('work-orders')

class UpdatePart(UpdateView):
    model = Appliances
    template_name = 'update_part.html'
    form_class = WorkOrderPartUpdate
    success_url = reverse_lazy('work-orders')