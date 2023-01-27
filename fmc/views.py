from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Work, Appliances
from .forms import WorkOrderForm, WorkOrderFormUpdate, WorkOrderPartAdd, WorkOrderPartUpdate
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Render PDF View
def work_order_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    work_order = get_object_or_404(Work, pk=pk)

    template_path = 'work_order_pdf.html'
    context = {'work_order': work_order}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download: 
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="work_order.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

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

    #rearrange
class WorkOrdersRearrange(ListView):
    model = Work
    template_name = 'rearrange.html'

# Delete 
class DeleteWorkOrder(DeleteView):
    model= Work
    template_name = 'delete_work_order.html'
    success_url = reverse_lazy('work-orders')
