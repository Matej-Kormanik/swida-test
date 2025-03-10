from rest_framework import serializers

from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True, read_only=True)  # Automatická serializácia waypointov
    class Meta:
        model = Order
        fields = '__all__'

