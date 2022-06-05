from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from plataforma.models import Cliente,Proveedor,Personal
from plataforma.forms import Form_Proveedor,Form_Cliente,Form_Personal

# Create your views here.

def inicio (request):
    
    return render(request,"inicio.html")

def cliente (request):
    cliente = Cliente.objects.all()
    dicc = {"cliente" : cliente}
    plantillas = loader.get_template("clientes.html")
    documento = plantillas.render(dicc) 
    return HttpResponse(documento)

def proveedor (request):
    proveedor = Proveedor.objects.all()
    dicc = {"proveedor" : proveedor}
    plantillas = loader.get_template("proveedores.html")
    documento = plantillas.render(dicc) 
    return HttpResponse(documento)

def personal (request):
    personal = Personal.objects.all()
    dicc = {"personal" : personal}
    plantillas = loader.get_template("personal.html")
    documento = plantillas.render(dicc) 
    return HttpResponse(documento)
   


def alta_personal (request):

    if request.method == "POST":
        
        mi_formulario = Form_Personal(request.POST)
        
        if mi_formulario.is_valid():

            datos= mi_formulario.cleaned_data
            print(datos)
            personal= Personal( nombreU= datos['nombreU'] , sector=datos['sector'] , rol=datos['rol'])
            personal.save()
            return render(request,"cargaok.html")
          
    
    return render(request,"form_personal.html")

def alta_cliente (request):

    if request.method == "POST":
        
        mi_formulario = Form_Cliente(request.POST)
        
        if mi_formulario.is_valid():

            datos= mi_formulario.cleaned_data
            print(datos)
            personal= Cliente( nombreC= datos['nombreC'] , tipo_cli=datos['tipo_cli'] , rama=datos['rama'])
            personal.save()
            return render(request,"cargaok.html")
          
    
    return render(request,"form_cliente.html")

def alta_proveedor (request):

    if request.method == "POST":
        
        mi_formulario = Form_Proveedor(request.POST)
        
        if mi_formulario.is_valid():

            datos= mi_formulario.cleaned_data
            print(datos)
            personal= Proveedor( nombreP= datos['nombreP'] , codigoprov=datos['codigoprov'] , tipo_prov=datos['tipo_prov'],rama=datos['rama'])
            personal.save()
            return render(request,"cargaok.html")
        
    
    return render(request,"form_proveedor.html")

    

def buscar (request):

    if request.method== "POST":
        rama = request.POST ['rama']
        print(rama)
        rama = Proveedor.objects.filter(rama__icontains =rama)
        print(rama)
        rama2= Cliente.objects.filter(rama__icontains=rama)
        return render (request, "buscarama.html",{"rama":rama,"rama2":rama2})
    else:
        return render(request,"buscar.html")
    
    

