from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            pass_word = check_password(password,customer.password)
            if pass_word:
                request.session["customer_id"] = customer.id
                request.session["email"] = customer.email

                return redirect("home")
            else:
                error_message = "Email or Password invalid"
        else:
            error_message = "Email or Password invalid"
        # print(customer)
        print(email,password)

        return render(request,"login.html",{"error": error_message})


def logout(request):
    request.session.clear()
    return redirect("login")