from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils import timezone

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    user_permissions = None
    groups = None

    def __str__(self):
        return f'{self.username}{self.first_name}{self.last_name}'

class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile_user", on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default="-")
    address = models.CharField(max_length=100, default="-")
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Token(models.Model):
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="-")
    price = models.FloatField(default=0.0)
    user_create = models.ForeignKey(User, related_name="user_create_room_type", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_room_type", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, related_name="room_type", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, default="Tersedia")
    user_create = models.ForeignKey(User, related_name="user_create_room", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_room", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Guest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="-")
    email = models.CharField(max_length=100, default="-")
    address = models.CharField(max_length=100, default="-")
    user_create = models.ForeignKey(User, related_name="user_create_guest", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_guest", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Booking(models.Model):
    guest = models.ForeignKey(Guest, related_name="booking_guest", null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, related_name="booking_room", null=True, blank=True, on_delete=models.SET_NULL)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")
    total_price = models.FloatField(default=0.0)
    user_create = models.ForeignKey(User, related_name="user_create_booking", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_booking", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(default="-")
    user_create = models.ForeignKey(User, related_name="user_create_service", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_service", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, related_name="payment_booking", null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0.0)
    method = models.CharField(max_length=50, default="Cash")
    status = models.CharField(max_length=20, default="Belum Lunas")
    paid_on = models.DateTimeField(null=True, blank=True)
    user_create = models.ForeignKey(User, related_name="user_create_payment", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_payment", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
