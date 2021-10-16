from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Products


# Create your views here.
@login_required
def products(request):
    product_dict = Products.objects.all()
    return render(request, template_name="products/products.html", context={"context": product_dict})


@login_required
def product_details(request, product_id):
    single_product = Products.objects.get(product_id=product_id)
    single_product.viewCount += 1
    single_product.save()
    return render(request, template_name="products/product_details.html", context={"context": single_product})
