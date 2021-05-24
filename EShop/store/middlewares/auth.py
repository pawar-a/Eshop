from django.shortcuts import render,HttpResponse,redirect

def auth_middlewares(get_response):

    def middleware(request):
        print("middaleware")
        print(request.session.get("customer_id"))
        returnUrl = request.META["PATH_INFO"]
        
        response =  get_response(request)
        if not request.session.get("customer_id"):
            return redirect(f"login?return_url={returnUrl}")

        return response

    return middleware