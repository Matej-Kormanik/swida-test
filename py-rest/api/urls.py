from django.urls import path
from . import views
from .views import OrderView

urlpatterns = [
    path('orders/', views.OrderView.as_view(), name='order-view'),
    # path('blogposts/<int:pk>', views.BlogPostDeleteDestroyAPIView.as_view(), name='blogpost-delete-view'),
]
