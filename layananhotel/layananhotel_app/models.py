from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}{self.first_name}{self.last_name}'

class Profile(models.Model):
    code = models.CharField(max_length=20)
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
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(default="-")
    price = models.FloatField(default=0.0)
    user_create = models.ForeignKey(User, related_name="user_create_room_type", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_room_type", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Room(models.Model):
    status_choice=(
        ("Tersedia","Tersedia"),
        ("Tidak Tersedia","Tidak Tersedia")
    )

    code = models.CharField(max_length=20)
    room_type = models.ForeignKey(RoomType, related_name="room_type", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20,choices=status_choice, default="Tersedia")
    user_create = models.ForeignKey(User, related_name="user_create_room", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_room", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Booking(models.Model):
    status_choice=(
        ("Pending","Pending"),
        ("Confirm","Confirm"),
        ("Cancel","Cancel")
    )


    code = models.CharField(max_length=20)   
    name_customer = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="-")
    email = models.CharField(max_length=100, default="-")
    address = models.CharField(max_length=100, default="-")
    room = models.ForeignKey(Room, related_name="booking_room", null=True, blank=True, on_delete=models.SET_NULL)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20,choices=status_choice, default="Pending")
    user_create = models.ForeignKey(User, related_name="user_create_booking", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_booking", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Service(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(default="-")
    user_create = models.ForeignKey(User, related_name="user_create_service", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_service", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

class Payment(models.Model):
    method_choice=(
        ("Cash","Cash"),
        ("Transfer","Transfer"),
    )

    status_choice=(
        ("Belum Lunas","Belum Lunas"),
        ("Lunas","Lunas"),
    )
    code = models.CharField(max_length=20)
    booking = models.ForeignKey(Booking, related_name="payment_booking", null=True, blank=True, on_delete=models.SET_NULL)
    jumlah = models.FloatField(default=0.0)
    method = models.CharField(max_length=50,choices=method_choice, default="Cash")
    status = models.CharField(max_length=20,choices=status_choice, default="Belum Lunas")
    user_create = models.ForeignKey(User, related_name="user_create_payment", null=True, blank=True, on_delete=models.SET_NULL)
    user_update = models.ForeignKey(User, related_name="user_update_payment", null=True, blank=True, on_delete=models.SET_NULL)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
