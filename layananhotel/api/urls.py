from django.urls import path,include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    RoomGetPost, RoomGetUpDel,
    RoomTypeGet, BookingGetPost, BookingGetUpDel,
    ServiceGet, PaymentPost, ProfileGetUpDel
)

app_name = 'api'

urlpatterns = [
    path('api/room_list', RoomGetPost.as_view()),
    path('api/room_detail/<int:pk>', RoomGetUpDel.as_view()),

    path('api/roomtype_list', RoomTypeGet.as_view()),

    path('api/booking_list', BookingGetPost.as_view()),
    path('api/booking_detail/<int:pk>', BookingGetUpDel.as_view()),

    path('api/service_list', ServiceGet.as_view()),

    path('api/payment_add', PaymentPost.as_view()),

    path('api/profile_detail/<int:pk>', ProfileGetUpDel.as_view()),
]
