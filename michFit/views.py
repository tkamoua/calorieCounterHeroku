from django.shortcuts import render
import smtplib

from django.http import HttpResponse, Http404
from .models import MenuItem
from . import calorieCounter
cart = []
totalCalories = 0
totalProtein = 0
def home(request):
    menu = MenuItem.objects.all()
    context = {'menu': menu}
    MenuItem.objects.all().delete()
    for key, value in calorieCounter.itemsDict.items():
        MenuItem.objects.create_item(key, value[0],value[1])
    return render(request,'michFit/index.html',context)


def cartdelete(request, item_id):
    try:
        print(cart)
        cart.remove(MenuItem.objects.get(pk=item_id))
        totalCalories = 0
        totalProtein=0
        for item in cart:
            totalCalories += item.calories
            totalProtein+=item.protein
        return render(request, 'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )
    except:
        print(cart)
        totalCalories = 0
        totalProtein=0
        for item in cart:
            totalCalories += item.calories
            totalProtein+=item.protein
        return render(request, 'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )
    

def cart_add( request,item_id):
    cart.append(MenuItem.objects.get(pk=item_id))
    menu = MenuItem.objects.all()
    context = {'menu': menu}
    return render(request,'michFit/index.html',context)
    
    
   
    
def cart_view(request,item_id):

    totalCalories = 0
    totalProtein=0
    for item in cart:
        totalCalories += item.calories
        totalProtein+=item.protein
    return render(request, 'michFit/cart.html',{'cart': cart, 'totalCalories': totalCalories, 'totalProtein': totalProtein} )

def send_email(request):
    print('send email view')
    names=[]
    for item in cart:
        names.append(item.name)
    print(names)
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    print('smtplib.SMTP')
    smtpObj.ehlo()
    print('smtpObj.ehlo')
    smtpObj.starttls()
    print('starttls')
    smtpObj.login('tkamoua@gmail.com',input())

    print('Login success')
    smtpObj.sendmail('tkamoua@gmail.com','tkamoua@umich.edu','Subject: Menu. \n\n %s' %(names))
    print('sent email')
    smtpObj.quit()
    return HttpResponse("Email sent")