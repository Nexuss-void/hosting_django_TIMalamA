from rest_framework import serializers
from layananhotel_app.models import User, Profile, RoomType, Room, Booking, Service, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'address']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'price', 'description']

class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.PrimaryKeyRelatedField(queryset=RoomType.objects.all())

    class Meta:
        model = Room
        fields = ['id', 'number', 'room_type', 'status']

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    check_in = serializers.DateTimeField()
    check_out = serializers.DateTimeField()
    status = serializers.CharField()

    class Meta:
        model = Booking
        fields = ['id', 'code', 'guest', 'room', 'check_in', 'check_out', 'status']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'code', 'name', 'price', 'description']

class PaymentSerializer(serializers.ModelSerializer):
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all())
    amount = serializers.FloatField()
    method = serializers.CharField()
    status = serializers.CharField()
    payment_date = serializers.DateTimeField()

    class Meta:
        model = Payment
        fields = ['id', 'booking', 'amount', 'method', 'status', 'payment_date']
