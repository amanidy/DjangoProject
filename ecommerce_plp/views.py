from django.shortcuts import render, get_object_or_404
from .models import Product,Customer


# Create your views here.
# Product View
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'Ecommerce/product_list.html',context)


def product_detail(request,pk):
  product = get_object_or_404(Product, pk=pk)
  context = {
        'product': product
    }
  return render(request,'Ecommerce/product_detail.html',context)

  #Customer view
def customer_list(request):
   customers = Customer.objects.all()
   context = {
      'customers': customers
   }
   return render(request, 'Ecommerce/customer_list.html', context)

def customer_detail(request,pk):
   customer = get_object_or_404(Customer, pk=pk)
   context ={
      'customer':customer
   }
   return render(request,'Ecommerce/customer_detail.html',context)