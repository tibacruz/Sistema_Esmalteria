from django.shortcuts import render,redirect,get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages

def lista_de_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request,"clientes/lista_de_clientes.html",{'clientes':clientes})

def adicionar_cliente(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ClienteForm()
        messages.success(request,"Cliente adicionado com sucesso")
        return redirect('lista_de_clientes')

    return render(request,"clientes/adicionar_cliente.html",{'form':form})

def editar_cliente(request,id=None):
    cliente = get_object_or_404(Cliente,id=id)
    form = ClienteForm(request.POST or None,instance=cliente)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Cliente editado com sucesso")
        return redirect('lista_de_clientes')
        
    return render(request,"clientes/editar_cliente.html",{'form':form})

def remover_cliente(request,id=None):
    cliente = get_object_or_404(Cliente,id=id)
    if request.method == "POST":
        cliente.delete()
        messages.warning(request,"Cliente removido com sucesso")
        return redirect('lista_de_clientes')

    return render(request,"clientes/remover_cliente.html",{'cliente':cliente})
