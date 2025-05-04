from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test


def productsList(request):
    products = Product.objects.all()
    return render(request, 'products/productsList.html', {'products': products})

@user_passes_test(lambda u: u.is_superuser)
def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.save()
            return redirect('managerProduct')
    else:
        form = ProductForm()
        return render(request, 'products/productRegister.html', {'form': form})

def updateProduct(request, id):
    register = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, request.FILES or None,instance=register)
    if form.is_valid():
        form.save()
        return redirect('managerProduct')
    return render(request, 'products/updateProduct.html', {'register': register, 
                                                         'form':form})

@user_passes_test(lambda u: u.is_superuser)
def delProduct(request, id):
    register = Product.objects.get(id=id)
    register.delete()
    return redirect('managerProduct')                                                        

@user_passes_test(lambda u: u.is_superuser)
def manager(request):
    services = Product.objects.all().order_by('-id')
    return render(request, 'products/managerProduct.html', {'services':services})