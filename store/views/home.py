from django.shortcuts import render, redirect

# Create your views here.
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from store.models.slider import Slider

class Store(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')


        if cart:
            quantity = cart.get(product)

            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:

                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Category.objects.all()
        categoryId = request.GET.get('category')
        sliders = Slider.objects.all()

        if categoryId:
            products = Product.get_all_products_by_category_id(categoryId)
        else:
            products = Product.objects.all()

        templates = 'index.html'
        context = {
            'products': products,
            'categories': categories,
             'sliders': sliders

        }

        return render(request, templates, context)
