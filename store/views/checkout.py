from django.shortcuts import render, redirect

# Create your views here.
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer)
        if customer:

            for product in products:
                order = Order(customer=customer,
                              product=product,
                              brandname=product.brandname,
                              variety=product.variety,
                              weight=product.weight,
                              price=product.price,
                              address=address,
                              phone=phone,
                              quantity=cart.get(str(product.id)))

                order.save();

            request.session['cart'] = {}
            return redirect('cart')

        else:
            return redirect('login')
