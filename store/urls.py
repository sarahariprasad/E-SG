from django.urls import path
from .views.home import Store
from .views.register import Register
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

from django.contrib.auth import views as auth_views
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Store.as_view(), name='homepage'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='password_resetdone.html'),
         name='password_reset_done'),
    path('password_reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset-confirm'),
    path('password_reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset-complete'),
]
