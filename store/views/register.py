from django.shortcuts import render, redirect

# Create your views here.
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST

        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        print(first_name)
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:
            print('first_name', 'last_name', 'phone', 'email', 'password')
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'register.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = 'First Name Required !!'

        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char or more long'

        elif not customer.last_name:
            error_message = 'Last Name Required !!'

        elif len(customer.last_name) < 1:
            error_message = 'Last Name must be 1 char or more long'

        elif not customer.phone:
            error_message = 'Phone Number Required !!'

        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char or more long'

        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char or more long'

        elif not customer.password:
            error_message = 'Password Required !!'

        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char or more long'

        elif customer.isExists():
            error_message = 'Phone Number or Email Address Already Registered..'
        return error_message
        # saving
