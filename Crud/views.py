from itertools import product
from django.shortcuts import render, redirect
from .models import Producto
from Crud.forms import ProductoForm

#class Producto:
    #def __init__(self,nombre,valor):
        #self.nombre = nombre
        #self.valor = valor
        #super().__init__()



# Create your views here.

#def home(request):

    #vinilo = Producto("Vinilo de Black Albun",19990)


    #lista = ["Goku","Vegueta","Picoro","Krilin"]
    #contex = {"nombre":"Dayana Granadillo","personajes":lista,"vinilo":vinilo}
    #return render(request,'crud/home.html',contex)

def home(request):
    productos = Producto.objects.all()
    contexto = {
        'productos':productos
    }
    return render(request,'crud/home.html',contexto)


def form_producto(request):

    contexto = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
        

    return render(request,'crud/form_producto.html',contexto)


def form_mod_producto(request,id):
    producto = Producto.objects.get(idProducto = id)
    
    
    contexto = {
        'form' : ProductoForm(instance=producto)
        
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"
            
            
    return render (request,'crud/form_mod_producto.html',contexto)


def form_del_producto(request,id):
    producto = Producto.objects.get(idProducto = id)
    
    producto.delete()
    
    return redirect (to="home")
    