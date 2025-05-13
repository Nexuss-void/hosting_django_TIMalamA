from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework import permissions
from layananhotel_app.models import User, Profile, RoomType, Room, Booking, Service, Payment
from api.serializers import (
    UserSerializer, ProfileSerializer, RoomTypeSerializer,
    RoomSerializer, BookingSerializer, ServiceSerializer, PaymentSerializer
)

class RoomGetPost(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomTypeGet(ListAPIView):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()

class BookingGetPost(ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class ServiceGet(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class PaymentPost(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class ProfileGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
