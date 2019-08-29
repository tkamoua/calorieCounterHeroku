from django.urls import path

from . import views


app_name = 'michFit'
urlpatterns = [
    path('', views.home, name='home'),
    path('cart_add/<item_id>/',views.cart_add, name='cart_add'),
    path('cart/view/<item_id>/',views.cart_view, name='cartview'),
    path('cartdelete/<item_id>/',views.cartdelete, name='cartdelete'),
    path('sendemail/',views.send_email,name='sendemail')
]