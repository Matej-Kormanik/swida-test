from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import OrderSerializer
from .models import Order, Waypoint
from .serializers import WaypointSerializer


# class BlogPostListCreateAPIView(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#
#     def delete(self, request, *args, **kwargs):
#         BlogPost.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class BlogPostDeleteDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     lookup_field = 'pk'

class OrderView(APIView):
    def get(self, request, format=None):
        order_number = request.query_params.get('order_number', '')
        if order_number:
            orders = Order.objects.filter(number__icontains=order_number)
        else:
            orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Uloží nový Order do databázy
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WaypointListCreateView(APIView):
    def get(self, request, order_id):
        """Získa zoznam všetkých waypointov pre danú objednávku."""
        waypoints = Waypoint.objects.filter(order_id=order_id)
        serializer = WaypointSerializer(waypoints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, order_id):
        """Vytvorí nový waypoint pre danú objednávku."""
        order = get_object_or_404(Order, id=order_id)  # Overenie, či objednávka existuje
        serializer = WaypointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(order=order)  # Uloženie s priradeným order_id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
