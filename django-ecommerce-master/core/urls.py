from django.urls import path
from .views import (
    ItemDetailView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    ProductsView,
    about,
    add_single_item_to_cart,
    remove_all_items_from_cart,
    ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/<int:count>/', add_to_cart, name='add-to-cart'),
    path('add-single-item-to-cart/<slug>/', add_single_item_to_cart,
         name='add-single-item-to-cart'),
    path('remove-from-cart/<slug>/<int:count>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('remove-all-items-from-cart/<slug>/', remove_all_items_from_cart,
         name='remove-all-items-from-cart'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<main_id>/', ProductsView.as_view(), name='show-main-category'),
    path('products/<main_id>/<sub_id>', ProductsView.as_view(), name='show-sub-category'),
    path('about-us/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]

app_name = 'core'



