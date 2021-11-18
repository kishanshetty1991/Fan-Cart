from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Order,Contact
import math
import json
import datetime
import calendar
# Create your views here.
def index(request):
	allProds = []
	allcats = models.Product.objects.values('category','product_id')
	cats = {item['category'] for item in allcats}
	for cat in cats:
		prod = models.Product.objects.filter(category = cat)
		nslide = math.ceil(len(prod)/4)
		allProds.append([prod,range(1,nslide),nslide])
	params = {'allProds': allProds}
	return render (request, 'shop/index.html',params)


def about(request):
	return render(request,'shop/about.html')


#To get data from contact.html
def contact(request):
	cname=email=phone=desc=""
	if request.method == "POST":
		cname = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		desc = request.POST.get('desc','')
		#To add data to database (here Contact model)   
		contact = Contact(name=cname,email=email,phone=phone,desc=desc)
		contact.save()
		return render(request,'shop/contact.html')  
	return render(request,'shop/contact.html')      



def tracker(request):
	order_id = email = myDate = formatedDate= ""
	if request.method == 'POST':
		order_id = request.POST.get('order_id','')
		email = request.POST.get('email')
		myDate = datetime.datetime.now()
		formatedDate = myDate.strftime("%d-%B-%Y  %H:%M:%S %A")
		# calendarDate = formatDate.strftime('%A')
		# formatedDate = f"Day: {calendarDate} Date:{formatDate}"
		try:
			order = Order.objects.filter(order_id=order_id)
			if len(order) > 0:
				update = models.OrderUpdate.objects.filter(order_id=order_id)
				updates = []
				for item in update:
					updates.append({'text': item.update_desc, 'time': formatedDate})
					response = json.dumps([updates,order[0].item_json], default=str)
				return HttpResponse(response)
			else:
				return HttpResponse('{}')
		except Exception as e:
			return HttpResponse('{}')
	return render(request,'shop/tracker.html')  


def product(request, myid):
	product = models.Product.objects.get(product_id = myid)
	params ={
	"product": product
	}
	return render(request,'shop/product.html',params)


def search(request):
	return HttpResponse("<h1 align='center'>Search</h1>")


def checkout(request):
	item_json=name=email=phone=address=city=state=zip_code=""
	if request.method == "POST":
		item_json = request.POST.get('itemsJson','')
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		address = request.POST.get('address1','') + " " + request.POST.get('address2','')
		city = request.POST.get('city','')
		state = request.POST.get('state','')
		zip_code = request.POST.get('zip_code','')
		phone = request.POST.get('phone','')


		#To add data to database (here Order model) 
		order = Order(item_json=item_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
		order.save()
		update = models.OrderUpdate(order_id=order.order_id,update_desc="This Order has been Placed")
		update.save()
		thank = True
		id1 = order.order_id
		return render(request,'shop/checkout.html',{'thank':thank,'id':id1})
	return render(request, 'shop/checkout.html')        
