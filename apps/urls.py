
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ProductListView, ProductDetailTemplateView, RegisterCreateView, \
    SettingsUpdateView, FavouriteView, CartListView, CartItemDeleteView, AddToCartView, CustomLogoutView, \
    CheckoutListView, AddressCreateView, AddressUpdateView


urlpatterns = [
    # path('rv/', ProductLIstTemplateView.as_view(), name='product_list'),
    path('', ProductListView.as_view(), name='product_list_page'),
    path('product-detail/<int:pk>/', ProductDetailTemplateView.as_view(), name='product_detail'),

    path('settings', SettingsUpdateView.as_view(), name='settings_page'),
    path('register', RegisterCreateView.as_view(), name='register_page'),

    path('login', LoginView.as_view(
        template_name='apps/auth/login.html',
        redirect_authenticated_user=True
    ), name='login_page'),
    path('logout', CustomLogoutView.as_view(template_name='apps/auth/login.html'), name='logout_page'),

    path('shopping_cart', CartListView.as_view(), name='shopping_cart_page'),
    path('remove-cart/<int:pk>/', CartItemDeleteView.as_view(), name='delete_cart_item'),
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_cart_page'),

    path('favorite/<int:pk>', FavouriteView.as_view(), name='add_favorite'),

    path('checkout', CheckoutListView.as_view(), name='checkout_page'),

    path('addres-create', AddressCreateView.as_view(), name='address_page'),
    path('address-update/<int:pk>/', AddressUpdateView.as_view(), name='update_address'),
    

]
