from django.shortcuts import render, HttpResponse, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.

class Index(View):
    def get(self,request):
        cart = request.session.get("cart")
        if not cart:
            request.session.cart = {}
        products = None
        categories = Category.get_all_categories()
        categoryid = request.GET.get("category")
        if categoryid:
            products = Product.get_all_product_by_categoryid(categoryid)
        else:
            products = Product.get_all_products()
        data = {}
        data["products"] = products
        data["categories"] = categories
        print("your email",request.session.get("email"))
        print("your id",request.session.get("customer_id"))
        return render(request, 'index.html', data)

    def post(self,request):
        product = request.POST.get("product_id")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] -= 1    
                else:
                    cart[product] += 1
            else:
                cart[product] = 1
        else:
            cart ={}
            cart[product] = 1
        print(product)

        request.session["cart"] = cart
        print(request.session["cart"] )
        return redirect("home")

# def index(request):
    

# def login(request):
#     if request.method == "GET":

#     else:


# def signup(request):
#     print("call")
#     if request.method == "GET":
