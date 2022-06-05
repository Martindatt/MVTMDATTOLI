from django.urls import path
from . import views

urlpatterns = [

    path ("",views.inicio, name='inicio'),
    path("clientes",views.cliente, name='clientes'),
    path("proveedores",views.proveedor, name='proveedores'),
    path("personal",views.personal, name='personal'),
    path("form_personal",views.alta_personal),
    path("form_cliente",views.alta_cliente),
    path("form_proveedor",views.alta_proveedor),
    path("buscar",views.buscar, name='buscar' ),

]