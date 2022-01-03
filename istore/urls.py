from django.urls import path
from . import views

app_name = 'istore'
urlpatterns = [
   path('product-page',views.LatestProductView,name='home'),
   path('product/desc/<slug:slug>', views.DescriptionView, name="desc"),
   path('view-cart', views.ViewCart, name="view-cart")
]