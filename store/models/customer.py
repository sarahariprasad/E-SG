from django.db import models
from django.shortcuts import render, redirect


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):

        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def get_customers_by_id(customer):
        return Customer.objects.filter(customer=customer)

    def isExists(self):
        a = Customer.objects.filter(phone=self.phone)
        b = Customer.objects.filter(email=self.email)

        if a or b:
            print(a)
            print(b)
            return True
        else:
            return False
