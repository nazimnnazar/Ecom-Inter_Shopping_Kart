from django.urls import path
from.import views

urlpatterns=[
    path('cartDetails/', views.cartdetails, name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='mincart'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
]