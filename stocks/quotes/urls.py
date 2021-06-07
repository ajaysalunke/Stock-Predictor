from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url('add_stock.html',views.add_stock, name="add_stock"),
	url('delete_stock.html',views.delete_stock, name="delete_stock"),
	path('delete/<stock_id>' , views.delete, name="delete"),
	url('predict.html',views.predict, name="predict"),
]