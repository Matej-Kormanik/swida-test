from django.urls import path
from . import views
from .views import OrderView

urlpatterns = [
    path('orders/', views.OrderView.as_view(), name='order-view'),
    path('orders/<int:order_id>/waypoints/', views.WaypointListCreateView.as_view(), name='waypoint-list-create')
    # path('blogposts/<int:pk>', views.BlogPostDeleteDestroyAPIView.as_view(), name='blogpost-delete-view'),
]
