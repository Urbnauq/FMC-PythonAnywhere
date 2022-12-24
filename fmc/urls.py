from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, WorkOrders, WorkOrderDetails, CreateWorkOrder, UpdateWorkOrder, UpdatePart

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.index, name='home'),
    path('work_orders/', WorkOrders.as_view(), name='work-orders'),
    path('work_orders_details/<int:pk>', WorkOrderDetails.as_view(), name='work-order-details'),
    path('create_work_order/', CreateWorkOrder.as_view(), name='create-work-order'),
    path('edit_work_order/<int:pk>', UpdateWorkOrder.as_view(), name='update-work-order'),
    path('edit_appliance/<int:pk>', UpdatePart.as_view(), name='update-appliance-part'),

]