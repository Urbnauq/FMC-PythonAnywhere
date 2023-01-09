from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Work, Appliances
from .forms import WorkOrderForm, WorkOrderFormUpdate, WorkOrderPartAdd, WorkOrderPartUpdate
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy

#def home(request):
#   return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})

def search_orders(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        orders = Work.objects.filter(address__contains=searched) | Work.objects.filter(apartment__contains=searched) | Work.objects.filter(phone__contains=searched) | Work.objects.filter(date_added__contains=searched)

        return render(request, 'search.html', {
            'searched': searched,
            'orders': orders
        })
    else:
        return (request, 'search.html', {})

def autosuggest(request):  
    query_original = request.GET.get('term')
    queryset = Work.objects.filter(address__icontains=query_original) | Work.objects.filter(apartment__icontains=query_original) | Work.objects.filter(phone__icontains=query_original) | Work.objects.filter(date_added__icontains=query_original)
    mylist=[]
    mylist += [x.address for x in queryset]
    return JsonResponse(mylist, safe=False)

class WorkOrders(ListView):
    model = Work
    template_name = 'work_orders.html'
    ordering = ['-date_added']

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
    #success_url = reverse_lazy('work-orders')
    
    def get_success_url(self):
        return reverse_lazy('work-order-details', kwargs={'pk': self.object.pk})

class AddPart(CreateView):
    model = Appliances
    form_class = WorkOrderPartAdd
    template_name = 'add_part.html'
    
    def form_valid(self, form):
        form.instance.part_address_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('work-order-details', kwargs={'pk': self.kwargs['pk']})

class UpdatePart(SuccessMessageMixin, UpdateView):
    model = Appliances
    template_name = 'update_part.html'
    form_class = WorkOrderPartUpdate
    
    def get_success_message(self, cleaned_data):
        return 'Updated!'

    def get_success_url(self):
        return reverse_lazy('update-appliance-part', kwargs={'pk': self.object.pk})