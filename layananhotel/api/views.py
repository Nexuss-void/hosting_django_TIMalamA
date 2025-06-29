from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework import permissions
from layananhotel_app.models import User, Profile, RoomType, Room, Booking, Service, Payment
from api.serializers import (
    ProfileSerializer, RoomTypeSerializer,
    RoomSerializer, BookingSerializer, ServiceSerializer, PaymentSerializer
)

class RoomGetPost(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomTypeGetPost(ListCreateAPIView):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()

class RoomTypeGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()

class BookingGetPost(ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class ServiceGetPost(ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class PaymentGetPost(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PaymentGetUpDel(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
