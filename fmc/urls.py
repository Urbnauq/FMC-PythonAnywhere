from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, search_orders, autosuggest, work_order_render_pdf_view, WorkOrders, WorkOrderDetails, CreateWorkOrder, UpdateWorkOrder, AddPart, UpdatePart

urlpatterns = [
    
    #path('', views.home, name='home'),
    path('work_order_report/<pk>/', work_order_render_pdf_view, name='work-order-pdf'),
    #path('', views.index, name='home'),
    path('search_games', views.search_orders, name="search-orders"),
    path('autosuggest', views.autosuggest, name="autosuggest"),
    path('', WorkOrders.as_view(), name='work-orders'),
    path('work_orders_details/<int:pk>', WorkOrderDetails.as_view(), name='work-order-details'),
    path('create_work_order/', CreateWorkOrder.as_view(), name='create-work-order'),
    path('edit_work_order/<int:pk>', UpdateWorkOrder.as_view(), name='update-work-order'),
    path('work_orders_details/<int:pk>/add_part', AddPart.as_view(), name='add-part'),
    path('work_orders_details/<int:pk>/edit_part', UpdatePart.as_view(), name='update-appliance-part'),
    path('detele_work_order/<int:pk>/remove', views.DeleteWorkOrder.as_view(), name='delete-work-order'),
    
    # rearrange
    path('rearrange/', views.WorkOrdersRearrange.as_view(), name='work-orders-rearrange'),

    ]