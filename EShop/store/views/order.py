from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from store.models.orders import Order
from store.middlewares.auth import auth_middlewares
from django.utils.decorators import method_decorator


class OrderView(View):

    @method_decorator(auth_middlewares)

    def get(self,request):
        customer = request.session.get("customer_id")
        orders = Order.get_order_by_customer(customer)
        print(orders)
        return render(request,"order.html",{"order":orders})