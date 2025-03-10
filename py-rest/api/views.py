from rest_framework import generics, status
from rest_framework.response import Response
from api.models import Order
from api.serializers import OrderSerializer
from rest_framework.views import APIView

#
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