
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Producto
from .forms import ProductoForm
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

"""
class ProductoViewSet(viewsets.ViewSet):
    
    def create(self, request):
        
        serializer = ProductoSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return redirect('main')
        
        return Response(serializer.errors, status=400)
    
    
    def destroy(self, request, pk=None):
        
        try:
            
            producto = Producto.objects.get(pk=pk)
            
        except Producto.DoesNotExist:
            
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


# Create your views here.
def main(request):
    
    products = Producto.objects.all()
    
    context = {'products':products}
    
    return render(request, 'dynamic_table.html', context)


def product_form(request):
    
    context = {}
    
    if request.method == 'POST':
    
        url = 'http://localhost:8000/api/productos/'

        # Define the new data for the record
        data = {
            'nombre': request.POST['nombre'],
            'descripcion': request.POST['descripcion'],
            'precio':  request.POST['precio'],
            'cantidad':  request.POST['cantidad']
        }


        response = requests.post(url, json=data)


        if response.status_code == 201:
            return redirect('main')
        else:
            return Response(status=response.status_code)

    else:
    
        return render(request, 'add_product.html', context)



def edit_form(request, id):
    
    product = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        
        url = f'http://localhost:8000/api/productos/{id}/'
        
        data = {
            'nombre': request.POST['nombre'],
            'descripcion': request.POST['descripcion'],
            'precio':  request.POST['precio'],
            'cantidad':  request.POST['cantidad']
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            return redirect('main')
        else:
            return Response(status=response.status_code)

    
    else:
        
        context = {'product': product}
        
        return render(request, 'edit_product.html', context)
    


def delete_data(request, id):
    
    if request.method == 'POST':
        
        url = f'http://localhost:8000/api/productos/{id}'

        response = requests.delete(url)


        if response.status_code == 204: 
            return HttpResponseRedirect(reverse('main'))
        else:
            return Response(status=response.status_code)

    else:
        
        return HttpResponseRedirect(reverse('main'))
    
