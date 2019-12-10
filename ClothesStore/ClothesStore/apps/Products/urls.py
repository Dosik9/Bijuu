from django.urls import path, include
from . import views

app_name = 'Products'
urlpatterns = [
    path('', views.index, name='index'),
    path('women/', views.women_view, name='women'),
    path('kids/', views.kids_view, name='kids'),
    path('<int:product_id>/',views.detail, name="detail"),
    path('<int:product_id>/leave_comment', views.leave_comment, name="leave_comment"),
    path('search/<int:product_id>/', views.search, name='search'),
    path('add_to_cart/', views.add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart_view, name='remove_from_cart'),
    # path('change_item_qty/', change_item_qty, name='change_item_qty'),
    path('cart/', views.cart_view,name='cart'),
]
