from django import views
from django.urls import path
from .import views


urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('<slug:c_slug>/<slug:product_slug>', views.views, name='views'),
    path('signup/',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('servies',views.servies,name='servies'), 
    path('contact',views.contact,name='contact'),
]
