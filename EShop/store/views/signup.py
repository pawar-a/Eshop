from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Signup(View):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
        return self.registeruser(request)


    def registeruser(self,request):

        postData = request.POST
        first_name = postData.get("firstname")
        last_name = postData.get("lastname")
        phone = postData.get("phone")
        email = postData.get("email")
        password = postData.get("password")

        error_message = None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)

        #create dict
        value = {
            "first_name":first_name,
            "last_name":last_name,
            "phone":phone,
            "email":email
        }

        error_message = self.validateCustomer(customer)

        # print(first_name,last_name,phone,email,password)
        if not error_message:
            
            customer.password = make_password(customer.password)
            #save data on databse
            customer.register()

            return redirect("home")
        else:
            #create dict
            data = {
                "error": error_message,
                "values": value
            }
            return render(request,"signup.html",data)
    def validateCustomer(self,customer):
        error_message = None
        # validation
        if not customer.first_name:
            error_message = "First Name Is Required !!"
        elif len(customer.first_name) <4:
            error_message = "First name  is morthan 4 or more Char"
        elif not customer.last_name:
            error_message = "Last Name Is Required !!"
        elif len(customer.last_name)<3:
            error_message = "Last name  is morthan 4 or more Cahr !!"
        elif not customer.phone:
            error_message = "Phone Number Is Required !!"
        elif len(customer.phone)<8:
            error_message = "Phone number  is morthan 4 or more Number !!"
        elif not customer.email:
            error_message = "Email Is Required !!"
        # elif len(email)<12:
        elif not  customer.password:
            error_message = "Password Is Required !!"
        elif len(customer.password)<7:
            error_message = "password  is morthan 7 or more Char !!"

        elif customer.isExsist():
            error_message = "Email id is alredy registered "
        return error_message
