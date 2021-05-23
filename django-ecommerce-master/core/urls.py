from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    UserProfileView,
    ProductsView,
    about
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),

    path('product-read-data/<slug>/', ItemDetailView.as_view(), name='product-read-data'),

    path('add-to-cart/<slug>/<int:count>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/<int:count>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('account/', UserProfileView.as_view(), name='account'),

    path('products/', ProductsView.as_view(), name='products'),

    path('products/<main_id>/', ProductsView.as_view(), name='show-main-category'),

    path('products/<main_id>/<sub_id>', ProductsView.as_view(), name='show-sub-category'),

    path('about-us/', about, name='about')
]
app_name = 'core'



