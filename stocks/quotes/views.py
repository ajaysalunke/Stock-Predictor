from django.http import request
from django.shortcuts import render,redirect
import fbprophet
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']

		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_19d0c9b014a3420d97d0254669d3d5ee")


		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api' : api })

	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above.."})


def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json
	
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Saved.."))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		output= []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_19d0c9b014a3420d97d0254669d3d5ee")


			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker' : ticker, 'output' : output })


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been Deleted!"))
	return redirect(add_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', { 'ticker' : ticker })


def predict(request):
	return render(request, "predict.html")
# def predict(request):
# 	def expensive_computation(a, b):
# 		if request.method == 'GET':
# 			time.sleep(2)  # 👈 This makes the function take 2s to run
# 			return a * b

# 	a = 2
# 	b = 21
# 	res = expensive_computation(a, b)

# 	st.write("Result:", res)
# 	return render(request, "predict.html", {"res": res})




