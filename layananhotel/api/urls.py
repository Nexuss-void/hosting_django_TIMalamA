from django.urls import path,include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    RoomGet,RoomPost, RoomGetUpDel,
    RoomTypeGetPost,RoomTypeGetUpDel,RoomFilterAPIView, BookingGetPost, BookingGetUpDel,
    ServiceGetPost,ServiceGetUpDel, PaymentGetPost,PaymentGetUpDel
)

app_name = 'api'

urlpatterns = [
    path('api/room_list', RoomGet.as_view()),
    path('api/room_create', RoomPost.as_view()),
    path('api/room_detail/<int:pk>', RoomGetUpDel.as_view()),

    path('api/roomtype_list', RoomTypeGetPost.as_view()),
    path('api/roomtype_detail/<int:pk>', RoomTypeGetUpDel.as_view()),
    path('api/room_filter/', views.RoomFilterAPIView.as_view(), name='menu-resto-filter'),


    path('api/booking_list', BookingGetPost.as_view()),
    path('api/booking_detail/<int:pk>', BookingGetUpDel.as_view()),

    path('api/service_list', ServiceGetPost.as_view()),
    path('api/service_detail/<int:pk>', ServiceGetUpDel.as_view()),

    path('api/payment_add', PaymentGetPost.as_view()),
    path('api/payment_detail/<int:pk>', PaymentGetUpDel.as_view()),
]
