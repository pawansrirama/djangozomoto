from django.urls import path
from .views import Dashboard,OrderDetials

urlpatterns = [
	path('dashboard/',Dashboard.as_view(),name='dashboard'),
	path('orders/<int:pk>/',OrderDetials.as_view(),name='order-detials')
	]