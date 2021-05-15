from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View



class Cart(View):
    def get(self,request):
        product_ids = list(request.session.get("cart").keys())
        products = Product.get_products_by_id(product_ids)

        print(products)

        return render(request,"cart.html",{"products":products})