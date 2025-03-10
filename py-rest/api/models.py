from django.db import models

class Order(models.Model):
    number = models.BigIntegerField()
    customer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Waypoint(models.Model):
    class WaypointType(models.TextChoices):
        PICKUP = "PICKUP", "Pickup"
        DELIVERY = "DELIVERY", "Delivery"

    location = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=WaypointType.choices
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="waypoints"
    )
