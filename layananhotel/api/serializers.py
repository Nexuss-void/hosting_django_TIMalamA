from rest_framework import serializers
from layananhotel_app.models import User, Profile, RoomType, Room, Booking, Service, Payment

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'address']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id','code', 'name','description', 'price', ]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','code', 'room_type', 'status']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    class Meta:
        model = Room
        fields = ['id','code', 'room_type', 'status']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id','code', 'name_customer','phone','email','address', 'room', 'check_in', 'check_out', 'status']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','code', 'name', 'price', 'description']

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id','code', 'booking', 'jumlah', 'method', 'status',]
